"""CLI commands for Health Journal."""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

from health_journal.journal import (
    calculate_stats,
    find_journal_entries,
    format_stats_output,
    parse_time_period,
)

logger = logging.getLogger(__name__)


def validate_mood(value: str) -> int:
    """Validate mood value.

    Args:
        value: Mood value as string

    Returns:
        Validated mood as integer

    Raises:
        ValueError: If mood is not in valid range
    """
    try:
        mood = int(value)
        if mood not in [-2, -1, 0, 1, 2]:
            raise ValueError(f"mood must be -2, -1, 0, 1, or 2 (got {mood})")
        return mood
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError(f"mood must be an integer (got '{value}')")
        raise


def validate_energy(value: str) -> int:
    """Validate energy value.

    Args:
        value: Energy value as string

    Returns:
        Validated energy as integer

    Raises:
        ValueError: If energy is not in valid range
    """
    try:
        energy = int(value)
        if not 0 <= energy <= 10:
            raise ValueError(f"energy must be 0-10 (got {energy})")
        return energy
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError(f"energy must be an integer (got '{value}')")
        raise


def parse_comma_separated(value: str) -> list[str]:
    """Parse comma-separated string into list.

    Args:
        value: Comma-separated string

    Returns:
        List of strings with whitespace stripped, empty strings removed
    """
    if not value or not value.strip():
        return []
    items = [item.strip() for item in value.split(",")]
    return [item for item in items if item]


def get_interactive_input() -> dict:
    """Get input interactively from user.

    Returns:
        Dictionary with mood, energy, symptoms, meds, tags, note
    """
    print("体調ログを記録します（Ctrl+C で中断）")

    # Get mood
    while True:
        try:
            mood_str = input("気分 (-2=とても悪い, -1=悪い, 0=普通, 1=良い, 2=とても良い): ")
            mood = validate_mood(mood_str)
            break
        except ValueError as e:
            print(f"エラー: {e}")
            continue

    # Get energy
    while True:
        try:
            energy_str = input("エネルギー (0-10): ")
            energy = validate_energy(energy_str)
            break
        except ValueError as e:
            print(f"エラー: {e}")
            continue

    # Get symptoms
    symptoms_str = input("症状 (カンマ区切り、例: headache,nausea): ")
    symptoms = parse_comma_separated(symptoms_str)

    # Get meds (optional)
    meds_str = input("服薬 (カンマ区切り、任意): ")
    meds = parse_comma_separated(meds_str)

    # Get tags (optional)
    tags_str = input("タグ (カンマ区切り、任意): ")
    tags = parse_comma_separated(tags_str)

    # Get note
    print("メモ (複数行可、空行で終了):")
    lines = []
    while True:
        try:
            line = input()
            if not line:
                break
            lines.append(line)
        except EOFError:
            break
    note = "\n".join(lines)

    return {
        "mood": mood,
        "energy": energy,
        "symptoms": symptoms,
        "meds": meds,
        "tags": tags,
        "note": note,
    }


def generate_markdown(data: dict, timestamp: datetime) -> str:
    """Generate Markdown with YAML front matter.

    Args:
        data: Dictionary with mood, energy, symptoms, meds, tags, note
        timestamp: Timestamp with timezone

    Returns:
        Markdown string with YAML front matter
    """
    # Build front matter
    front_matter = {
        "schema": "health-journal/v1",
        "timestamp": timestamp.isoformat(),
        "mood": data["mood"],
        "energy": data["energy"],
        "symptoms": data["symptoms"],
    }

    # Add optional fields only if not empty
    if data.get("meds"):
        front_matter["meds"] = data["meds"]
    if data.get("tags"):
        front_matter["tags"] = data["tags"]

    # Generate YAML
    yaml_str = yaml.dump(
        front_matter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )

    # Build markdown
    markdown = f"---\n{yaml_str}---\n{data['note']}"
    return markdown


def get_journal_path(timestamp: datetime, base_dir: Path = None) -> Path:
    """Get journal file path based on timestamp.

    Args:
        timestamp: Timestamp with timezone
        base_dir: Base directory (default: journal/)

    Returns:
        Path to journal file
    """
    if base_dir is None:
        base_dir = Path("journal")

    # Format: journal/YYYY/MM/YYYY-MM-DDTHHMMSS+09:00.md
    year = timestamp.strftime("%Y")
    month = timestamp.strftime("%m")
    filename = timestamp.strftime("%Y-%m-%dT%H%M%S%z") + ".md"

    return base_dir / year / month / filename


def save_journal(markdown: str, path: Path) -> None:
    """Save journal to file.

    Args:
        markdown: Markdown content
        path: Path to save to
    """
    # Create directory if needed
    path.parent.mkdir(parents=True, exist_ok=True)

    # Save file
    path.write_text(markdown, encoding="utf-8")
    print(f"保存しました: {path}")


def cmd_wellness_log(args: argparse.Namespace) -> int:
    """Execute wellness log command.

    Args:
        args: Parsed arguments

    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        # Get timestamp (JST)
        timestamp = datetime.now(ZoneInfo("Asia/Tokyo"))

        # Get input
        if args.mood is not None:
            # Non-interactive mode
            try:
                data = {
                    "mood": validate_mood(str(args.mood)),
                    "energy": validate_energy(str(args.energy)),
                    "symptoms": parse_comma_separated(args.symptoms or ""),
                    "meds": parse_comma_separated(args.meds or ""),
                    "tags": parse_comma_separated(args.tags or ""),
                    "note": args.note or "",
                }
            except ValueError as e:
                print(f"エラー: {e}", file=sys.stderr)
                return 1
        else:
            # Interactive mode
            try:
                data = get_interactive_input()
            except (KeyboardInterrupt, EOFError):
                print("\n中断しました")
                return 1

        # Generate markdown
        markdown = generate_markdown(data, timestamp)

        # Dry-run or save
        if args.dry_run:
            print("=== Dry-run: 以下の内容が保存されます ===")
            print(markdown)
            journal_path = get_journal_path(timestamp)
            print(f"=== 保存先: {journal_path} ===")
        else:
            journal_path = get_journal_path(timestamp)
            save_journal(markdown, journal_path)

        return 0

    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        return 1


def cmd_wellness_stats(args: argparse.Namespace) -> int:
    """Execute wellness stats command.

    Args:
        args: Parsed arguments

    Returns:
        Exit code (0 for success)
    """
    try:
        # Setup logging
        logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")

        # Parse period
        period = args.since or "30d"
        try:
            delta = parse_time_period(period)
        except ValueError as e:
            print(f"エラー: {e}", file=sys.stderr)
            return 1

        # Calculate date range (JST)
        end_date = datetime.now(ZoneInfo("Asia/Tokyo"))
        start_date = end_date - delta

        # Find and parse entries
        base_dir = Path("journal")
        entries = find_journal_entries(base_dir, since=start_date)

        # Calculate stats
        stats = calculate_stats(entries)

        # Output
        output = format_stats_output(stats, period, start_date, end_date)
        print(output)

        return 0

    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        return 1


def cmd_wellness_list(args: argparse.Namespace) -> int:
    """Execute wellness list command.

    Args:
        args: Parsed arguments

    Returns:
        Exit code (0 for success)
    """
    try:
        # Setup logging
        logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")

        # Parse period
        period = args.since or "30d"
        try:
            delta = parse_time_period(period)
        except ValueError as e:
            print(f"エラー: {e}", file=sys.stderr)
            return 1

        # Calculate date range (JST)
        end_date = datetime.now(ZoneInfo("Asia/Tokyo"))
        start_date = end_date - delta

        # Find and parse entries
        base_dir = Path("journal")
        entries = find_journal_entries(base_dir, since=start_date)

        # Sort by timestamp (newest first)
        entries_sorted = sorted(
            [e for e in entries if e.timestamp is not None],
            key=lambda e: e.timestamp,
            reverse=True,
        )

        # Output
        for entry in entries_sorted:
            mood_str = f"mood={entry.mood:+d}" if entry.mood is not None else "mood=N/A"
            energy_str = f"energy={entry.energy}" if entry.energy is not None else "energy=N/A"
            print(f"{entry.timestamp.isoformat()}  {mood_str}  {energy_str}  {entry.path}")

        return 0

    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        return 1


def setup_wellness_parser(subparsers) -> None:
    """Setup wellness subcommand parser.

    Args:
        subparsers: Subparsers object from argparse
    """
    wellness_parser = subparsers.add_parser(
        "wellness",
        help="体調管理コマンド",
    )
    wellness_subparsers = wellness_parser.add_subparsers(dest="wellness_command")

    # wellness log subcommand
    log_parser = wellness_subparsers.add_parser(
        "log",
        help="体調ログを記録",
    )
    log_parser.add_argument(
        "--mood",
        type=int,
        help="気分 (-2..2)",
    )
    log_parser.add_argument(
        "--energy",
        type=int,
        help="エネルギー (0..10)",
    )
    log_parser.add_argument(
        "--symptoms",
        type=str,
        help="症状 (カンマ区切り)",
    )
    log_parser.add_argument(
        "--meds",
        type=str,
        help="服薬 (カンマ区切り、任意)",
    )
    log_parser.add_argument(
        "--tags",
        type=str,
        help="タグ (カンマ区切り、任意)",
    )
    log_parser.add_argument(
        "--note",
        type=str,
        help="メモ",
    )
    log_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="保存せずに内容を表示",
    )
    log_parser.set_defaults(func=cmd_wellness_log)

    # wellness stats subcommand
    stats_parser = wellness_subparsers.add_parser(
        "stats",
        help="統計情報を表示",
    )
    stats_parser.add_argument(
        "--since",
        type=str,
        help="期間指定 (例: 7d, 4w, 3m) デフォルト: 30d",
    )
    stats_parser.set_defaults(func=cmd_wellness_stats)

    # wellness list subcommand
    list_parser = wellness_subparsers.add_parser(
        "list",
        help="エントリ一覧を表示",
    )
    list_parser.add_argument(
        "--since",
        type=str,
        help="期間指定 (例: 7d, 4w, 3m) デフォルト: 30d",
    )
    list_parser.set_defaults(func=cmd_wellness_list)
