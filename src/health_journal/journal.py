"""Journal entry parsing and analysis."""

import logging
import re
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

import yaml

logger = logging.getLogger(__name__)


class JournalEntry:
    """Represents a parsed journal entry."""

    def __init__(self, path: Path, front_matter: dict, body: str):
        """Initialize journal entry.

        Args:
            path: Path to the journal file
            front_matter: Parsed YAML front matter
            body: Body text after front matter
        """
        self.path = path
        self.front_matter = front_matter
        self.body = body

    @property
    def timestamp(self) -> Optional[datetime]:
        """Get timestamp from front matter."""
        ts_str = self.front_matter.get("timestamp")
        if not ts_str:
            return None
        try:
            return datetime.fromisoformat(ts_str)
        except (ValueError, TypeError):
            return None

    @property
    def mood(self) -> Optional[int]:
        """Get mood from front matter."""
        return self.front_matter.get("mood")

    @property
    def energy(self) -> Optional[int]:
        """Get energy from front matter."""
        return self.front_matter.get("energy")

    @property
    def symptoms(self) -> list[str]:
        """Get symptoms from front matter (normalized to lowercase)."""
        syms = self.front_matter.get("symptoms", [])
        if not isinstance(syms, list):
            return []
        return [s.lower() for s in syms if isinstance(s, str)]

    @property
    def tags(self) -> list[str]:
        """Get tags from front matter (normalized to lowercase)."""
        tags = self.front_matter.get("tags", [])
        if not isinstance(tags, list):
            return []
        return [t.lower() for t in tags if isinstance(t, str)]


def parse_journal_entry(path: Path) -> Optional[JournalEntry]:
    """Parse a journal entry from file.

    Args:
        path: Path to journal markdown file

    Returns:
        JournalEntry if successful, None if parsing fails
    """
    try:
        content = path.read_text(encoding="utf-8")

        # Extract front matter between --- delimiters
        pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
        match = re.match(pattern, content, re.DOTALL)

        if not match:
            logger.warning(f"No front matter found in {path}")
            return None

        yaml_content = match.group(1)
        body = match.group(2).strip()

        # Parse YAML
        try:
            front_matter = yaml.safe_load(yaml_content)
            if not isinstance(front_matter, dict):
                logger.warning(f"Invalid front matter structure in {path}")
                return None
        except yaml.YAMLError as e:
            logger.warning(f"Failed to parse YAML in {path}: {e}")
            return None

        return JournalEntry(path, front_matter, body)

    except Exception as e:
        logger.warning(f"Failed to read {path}: {e}")
        return None


def parse_time_period(period: str) -> timedelta:
    """Parse time period string like '7d', '4w', '3m'.

    Args:
        period: Time period string (Nd, Nw, Nm)

    Returns:
        timedelta object

    Raises:
        ValueError: If period format is invalid
    """
    pattern = r"^(\d+)([dwm])$"
    match = re.match(pattern, period.lower())

    if not match:
        raise ValueError(f"Invalid period format: {period} (expected: Nd, Nw, or Nm)")

    value = int(match.group(1))
    unit = match.group(2)

    if unit == "d":
        return timedelta(days=value)
    elif unit == "w":
        return timedelta(weeks=value)
    elif unit == "m":
        return timedelta(days=value * 30)  # Approximate

    raise ValueError(f"Invalid period unit: {unit}")


def find_journal_entries(
    base_dir: Path, since: Optional[datetime] = None
) -> list[JournalEntry]:
    """Find and parse journal entries.

    Args:
        base_dir: Base journal directory (usually 'journal/')
        since: Only include entries after this datetime (inclusive)

    Returns:
        List of parsed journal entries
    """
    if not base_dir.exists():
        logger.info(f"Journal directory not found: {base_dir}")
        return []

    entries = []

    # Recursively find all .md files
    for md_file in base_dir.rglob("*.md"):
        entry = parse_journal_entry(md_file)
        if entry is None:
            continue

        # Filter by date if specified
        if since is not None:
            if entry.timestamp is None:
                logger.warning(f"Missing timestamp in {md_file}, skipping")
                continue
            if entry.timestamp < since:
                continue

        entries.append(entry)

    return entries


def calculate_stats(entries: list[JournalEntry]) -> dict:
    """Calculate statistics from journal entries.

    Args:
        entries: List of journal entries

    Returns:
        Dictionary with statistics
    """
    if not entries:
        return {
            "total_entries": 0,
            "avg_mood": None,
            "avg_energy": None,
            "top_symptoms": [],
            "top_tags": [],
        }

    # Calculate averages
    moods = [e.mood for e in entries if e.mood is not None]
    energies = [e.energy for e in entries if e.energy is not None]

    avg_mood = round(sum(moods) / len(moods), 2) if moods else None
    avg_energy = round(sum(energies) / len(energies), 2) if energies else None

    # Count symptoms and tags
    symptom_counter = Counter()
    tag_counter = Counter()

    for entry in entries:
        symptom_counter.update(entry.symptoms)
        tag_counter.update(entry.tags)

    # Get top 5 (sorted by count desc, then name asc)
    def get_top5(counter: Counter) -> list[tuple[str, int]]:
        return sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:5]

    return {
        "total_entries": len(entries),
        "avg_mood": avg_mood,
        "avg_energy": avg_energy,
        "top_symptoms": get_top5(symptom_counter),
        "top_tags": get_top5(tag_counter),
    }


def format_stats_output(stats: dict, period: str, start_date: datetime, end_date: datetime) -> str:
    """Format statistics for display.

    Args:
        stats: Statistics dictionary
        period: Period string (e.g., "30d")
        start_date: Start date of range
        end_date: End date of range

    Returns:
        Formatted string
    """
    lines = []
    lines.append(f"Range: last {period} (from {start_date.date()} to {end_date.date()} JST)")
    lines.append(f"Entries: {stats['total_entries']}")

    if stats["avg_mood"] is not None and stats["avg_energy"] is not None:
        lines.append(f"Avg mood: {stats['avg_mood']} / Avg energy: {stats['avg_energy']}")
    elif stats["avg_mood"] is not None:
        lines.append(f"Avg mood: {stats['avg_mood']} / Avg energy: N/A")
    elif stats["avg_energy"] is not None:
        lines.append(f"Avg mood: N/A / Avg energy: {stats['avg_energy']}")
    else:
        lines.append("Avg mood: N/A / Avg energy: N/A")

    # Format top symptoms
    if stats["top_symptoms"]:
        symptom_strs = [f"{name}({count})" for name, count in stats["top_symptoms"]]
        lines.append(f"Top symptoms: {', '.join(symptom_strs)}")
    else:
        lines.append("Top symptoms: (none)")

    # Format top tags
    if stats["top_tags"]:
        tag_strs = [f"{name}({count})" for name, count in stats["top_tags"]]
        lines.append(f"Top tags: {', '.join(tag_strs)}")
    else:
        lines.append("Top tags: (none)")

    return "\n".join(lines)
