"""Tests for journal parsing and analysis."""

import logging
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from health_journal.journal import (
    JournalEntry,
    calculate_stats,
    find_journal_entries,
    format_stats_output,
    parse_journal_entry,
    parse_time_period,
)


class TestParseTimePeriod:
    """Tests for parse_time_period function."""

    def test_parse_days(self):
        """Test parsing days."""
        assert parse_time_period("7d") == timedelta(days=7)
        assert parse_time_period("30d") == timedelta(days=30)

    def test_parse_weeks(self):
        """Test parsing weeks."""
        assert parse_time_period("4w") == timedelta(weeks=4)
        assert parse_time_period("1w") == timedelta(weeks=1)

    def test_parse_months(self):
        """Test parsing months (approximate)."""
        assert parse_time_period("3m") == timedelta(days=90)
        assert parse_time_period("1m") == timedelta(days=30)

    def test_case_insensitive(self):
        """Test that parsing is case insensitive."""
        assert parse_time_period("7D") == timedelta(days=7)
        assert parse_time_period("4W") == timedelta(weeks=4)
        assert parse_time_period("3M") == timedelta(days=90)

    def test_invalid_format(self):
        """Test invalid format raises ValueError."""
        with pytest.raises(ValueError, match="Invalid period format"):
            parse_time_period("7days")
        with pytest.raises(ValueError, match="Invalid period format"):
            parse_time_period("abc")
        with pytest.raises(ValueError, match="Invalid period format"):
            parse_time_period("")


class TestParseJournalEntry:
    """Tests for parse_journal_entry function."""

    def test_parse_valid_entry(self, tmp_path):
        """Test parsing a valid journal entry."""
        content = """---
schema: health-journal/v1
timestamp: '2025-10-30T21:37:00+09:00'
mood: 1
energy: 7
symptoms:
- headache
tags:
- work
---
Test note"""
        path = tmp_path / "test.md"
        path.write_text(content, encoding="utf-8")

        entry = parse_journal_entry(path)

        assert entry is not None
        assert entry.path == path
        assert entry.front_matter["mood"] == 1
        assert entry.front_matter["energy"] == 7
        assert entry.body == "Test note"

    def test_parse_entry_missing_fields(self, tmp_path):
        """Test parsing entry with missing optional fields."""
        content = """---
schema: health-journal/v1
timestamp: '2025-10-30T21:37:00+09:00'
symptoms: []
---
Test note"""
        path = tmp_path / "test.md"
        path.write_text(content, encoding="utf-8")

        entry = parse_journal_entry(path)

        assert entry is not None
        assert entry.mood is None
        assert entry.energy is None

    def test_parse_entry_no_front_matter(self, tmp_path, caplog):
        """Test parsing entry without front matter."""
        content = "Just plain text"
        path = tmp_path / "test.md"
        path.write_text(content, encoding="utf-8")

        with caplog.at_level(logging.WARNING):
            entry = parse_journal_entry(path)

        assert entry is None
        assert "No front matter found" in caplog.text

    def test_parse_entry_broken_yaml(self, tmp_path, caplog):
        """Test parsing entry with broken YAML."""
        content = """---
mood: 1
energy: 7
symptoms: [broken yaml
---
Test note"""
        path = tmp_path / "test.md"
        path.write_text(content, encoding="utf-8")

        with caplog.at_level(logging.WARNING):
            entry = parse_journal_entry(path)

        assert entry is None
        assert "Failed to parse YAML" in caplog.text


class TestJournalEntry:
    """Tests for JournalEntry class."""

    def test_timestamp_property(self):
        """Test timestamp property."""
        front_matter = {"timestamp": "2025-10-30T21:37:00+09:00"}
        entry = JournalEntry(Path("test.md"), front_matter, "body")

        ts = entry.timestamp
        assert ts is not None
        assert ts.year == 2025
        assert ts.month == 10
        assert ts.day == 30

    def test_timestamp_invalid(self):
        """Test invalid timestamp returns None."""
        front_matter = {"timestamp": "invalid"}
        entry = JournalEntry(Path("test.md"), front_matter, "body")

        assert entry.timestamp is None

    def test_symptoms_normalized(self):
        """Test symptoms are normalized to lowercase."""
        front_matter = {"symptoms": ["Headache", "NAUSEA", "Fatigue"]}
        entry = JournalEntry(Path("test.md"), front_matter, "body")

        assert entry.symptoms == ["headache", "nausea", "fatigue"]

    def test_symptoms_non_list(self):
        """Test non-list symptoms returns empty list."""
        front_matter = {"symptoms": "not a list"}
        entry = JournalEntry(Path("test.md"), front_matter, "body")

        assert entry.symptoms == []

    def test_tags_normalized(self):
        """Test tags are normalized to lowercase."""
        front_matter = {"tags": ["Work", "SLEEP", "Gym"]}
        entry = JournalEntry(Path("test.md"), front_matter, "body")

        assert entry.tags == ["work", "sleep", "gym"]


class TestFindJournalEntries:
    """Tests for find_journal_entries function."""

    def test_find_entries(self):
        """Test finding entries in fixtures directory."""
        base_dir = Path(__file__).parent / "fixtures" / "journal"
        entries = find_journal_entries(base_dir)

        # Should find valid entries, skip broken ones
        assert len(entries) >= 3  # At least 3 valid entries

    def test_find_entries_with_since(self):
        """Test filtering entries by date."""
        base_dir = Path(__file__).parent / "fixtures" / "journal"
        since = datetime(2025, 10, 26, tzinfo=ZoneInfo("Asia/Tokyo"))
        entries = find_journal_entries(base_dir, since=since)

        # Should only include entries >= 2025-10-26
        for entry in entries:
            if entry.timestamp:
                assert entry.timestamp >= since

    def test_find_entries_nonexistent_dir(self, tmp_path, caplog):
        """Test non-existent directory."""
        base_dir = tmp_path / "nonexistent"
        with caplog.at_level(logging.INFO):
            entries = find_journal_entries(base_dir)

        assert entries == []
        assert "not found" in caplog.text


class TestCalculateStats:
    """Tests for calculate_stats function."""

    def test_stats_empty(self):
        """Test stats with no entries."""
        stats = calculate_stats([])

        assert stats["total_entries"] == 0
        assert stats["avg_mood"] is None
        assert stats["avg_energy"] is None
        assert stats["top_symptoms"] == []
        assert stats["top_tags"] == []

    def test_stats_with_entries(self):
        """Test stats with valid entries."""
        entries = []

        # Entry 1
        front_matter1 = {
            "mood": 1,
            "energy": 7,
            "symptoms": ["headache"],
            "tags": ["work"],
        }
        entries.append(JournalEntry(Path("1.md"), front_matter1, ""))

        # Entry 2
        front_matter2 = {
            "mood": -1,
            "energy": 4,
            "symptoms": ["headache", "nausea"],
            "tags": ["work"],
        }
        entries.append(JournalEntry(Path("2.md"), front_matter2, ""))

        # Entry 3
        front_matter3 = {
            "mood": 0,
            "energy": 5,
            "symptoms": [],
            "tags": ["sleep"],
        }
        entries.append(JournalEntry(Path("3.md"), front_matter3, ""))

        stats = calculate_stats(entries)

        assert stats["total_entries"] == 3
        assert stats["avg_mood"] == 0.0  # (1 + -1 + 0) / 3
        assert stats["avg_energy"] == 5.33  # (7 + 4 + 5) / 3, rounded
        assert stats["top_symptoms"] == [("headache", 2), ("nausea", 1)]
        assert stats["top_tags"] == [("work", 2), ("sleep", 1)]

    def test_stats_missing_values(self):
        """Test stats with missing mood/energy values."""
        entries = []

        # Entry with mood only
        front_matter1 = {"mood": 1, "symptoms": [], "tags": []}
        entries.append(JournalEntry(Path("1.md"), front_matter1, ""))

        # Entry with energy only
        front_matter2 = {"energy": 7, "symptoms": [], "tags": []}
        entries.append(JournalEntry(Path("2.md"), front_matter2, ""))

        stats = calculate_stats(entries)

        assert stats["total_entries"] == 2
        assert stats["avg_mood"] == 1.0
        assert stats["avg_energy"] == 7.0

    def test_top5_sorted_correctly(self):
        """Test top 5 sorting (count desc, name asc)."""
        entries = []

        # Create entries with various symptoms
        symptoms_list = [
            ["a", "b", "c"],
            ["a", "b"],
            ["a", "d"],
            ["b", "d"],
            ["c", "d"],
            ["d", "e"],
        ]

        for symptoms in symptoms_list:
            front_matter = {"mood": 0, "energy": 5, "symptoms": symptoms, "tags": []}
            entries.append(JournalEntry(Path("test.md"), front_matter, ""))

        stats = calculate_stats(entries)

        # Expected: d(4), a(3), b(3), c(2), e(1)
        # For a and b with same count, alphabetical order
        top_symptoms = stats["top_symptoms"]
        assert top_symptoms[0] == ("d", 4)
        assert top_symptoms[1] == ("a", 3)
        assert top_symptoms[2] == ("b", 3)
        assert top_symptoms[3] == ("c", 2)
        assert top_symptoms[4] == ("e", 1)


class TestFormatStatsOutput:
    """Tests for format_stats_output function."""

    def test_format_output(self):
        """Test formatting stats output."""
        stats = {
            "total_entries": 27,
            "avg_mood": 0.37,
            "avg_energy": 6.85,
            "top_symptoms": [("headache", 6), ("nausea", 3), ("fatigue", 2)],
            "top_tags": [("work", 7), ("sleep", 5), ("gym", 3)],
        }

        start_date = datetime(2025, 9, 30, tzinfo=ZoneInfo("Asia/Tokyo"))
        end_date = datetime(2025, 10, 30, tzinfo=ZoneInfo("Asia/Tokyo"))

        output = format_stats_output(stats, "30d", start_date, end_date)

        assert "Range: last 30d (from 2025-09-30 to 2025-10-30 JST)" in output
        assert "Entries: 27" in output
        assert "Avg mood: 0.37 / Avg energy: 6.85" in output
        assert "Top symptoms: headache(6), nausea(3), fatigue(2)" in output
        assert "Top tags: work(7), sleep(5), gym(3)" in output

    def test_format_output_empty(self):
        """Test formatting empty stats."""
        stats = {
            "total_entries": 0,
            "avg_mood": None,
            "avg_energy": None,
            "top_symptoms": [],
            "top_tags": [],
        }

        start_date = datetime(2025, 10, 1, tzinfo=ZoneInfo("Asia/Tokyo"))
        end_date = datetime(2025, 10, 30, tzinfo=ZoneInfo("Asia/Tokyo"))

        output = format_stats_output(stats, "30d", start_date, end_date)

        assert "Entries: 0" in output
        assert "N/A" in output
        assert "(none)" in output
