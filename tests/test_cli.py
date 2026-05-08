"""Tests for CLI commands."""

import argparse
import sys
from datetime import datetime
from io import StringIO
from pathlib import Path
from unittest.mock import MagicMock, patch
from zoneinfo import ZoneInfo

import pytest

from health_journal.cli import (
    cmd_wellness_log,
    generate_markdown,
    get_interactive_input,
    get_journal_path,
    parse_comma_separated,
    save_journal,
    validate_energy,
    validate_mood,
)


class TestValidateMood:
    """Tests for validate_mood function."""

    def test_valid_mood_negative_two(self):
        """Test boundary: mood = -2."""
        assert validate_mood("-2") == -2

    def test_valid_mood_negative_one(self):
        """Test valid mood = -1."""
        assert validate_mood("-1") == -1

    def test_valid_mood_zero(self):
        """Test valid mood = 0."""
        assert validate_mood("0") == 0

    def test_valid_mood_positive_one(self):
        """Test valid mood = 1."""
        assert validate_mood("1") == 1

    def test_valid_mood_positive_two(self):
        """Test boundary: mood = 2."""
        assert validate_mood("2") == 2

    def test_invalid_mood_too_low(self):
        """Test invalid mood < -2."""
        with pytest.raises(ValueError, match="mood must be -2, -1, 0, 1, or 2"):
            validate_mood("-3")

    def test_invalid_mood_too_high(self):
        """Test invalid mood > 2."""
        with pytest.raises(ValueError, match="mood must be -2, -1, 0, 1, or 2"):
            validate_mood("3")

    def test_invalid_mood_not_integer(self):
        """Test invalid mood (not an integer)."""
        with pytest.raises(ValueError, match="mood must be an integer"):
            validate_mood("abc")

    def test_invalid_mood_float(self):
        """Test invalid mood (float)."""
        with pytest.raises(ValueError, match="mood must be an integer"):
            validate_mood("1.5")


class TestValidateEnergy:
    """Tests for validate_energy function."""

    def test_valid_energy_zero(self):
        """Test boundary: energy = 0."""
        assert validate_energy("0") == 0

    def test_valid_energy_five(self):
        """Test valid energy = 5."""
        assert validate_energy("5") == 5

    def test_valid_energy_ten(self):
        """Test boundary: energy = 10."""
        assert validate_energy("10") == 10

    def test_invalid_energy_negative(self):
        """Test invalid energy < 0."""
        with pytest.raises(ValueError, match="energy must be 0-10"):
            validate_energy("-1")

    def test_invalid_energy_too_high(self):
        """Test invalid energy > 10."""
        with pytest.raises(ValueError, match="energy must be 0-10"):
            validate_energy("11")

    def test_invalid_energy_not_integer(self):
        """Test invalid energy (not an integer)."""
        with pytest.raises(ValueError, match="energy must be an integer"):
            validate_energy("abc")

    def test_invalid_energy_float(self):
        """Test invalid energy (float)."""
        with pytest.raises(ValueError, match="energy must be an integer"):
            validate_energy("5.5")


class TestParseCommaSeparated:
    """Tests for parse_comma_separated function."""

    def test_empty_string(self):
        """Test empty string returns empty list."""
        assert parse_comma_separated("") == []

    def test_whitespace_only(self):
        """Test whitespace-only string returns empty list."""
        assert parse_comma_separated("   ") == []

    def test_single_item(self):
        """Test single item."""
        assert parse_comma_separated("headache") == ["headache"]

    def test_multiple_items(self):
        """Test multiple items."""
        assert parse_comma_separated("headache,nausea,fatigue") == [
            "headache",
            "nausea",
            "fatigue",
        ]

    def test_items_with_spaces(self):
        """Test items with spaces are trimmed."""
        assert parse_comma_separated(" headache , nausea , fatigue ") == [
            "headache",
            "nausea",
            "fatigue",
        ]

    def test_empty_items_removed(self):
        """Test empty items are removed."""
        assert parse_comma_separated("headache,,nausea") == ["headache", "nausea"]

    def test_trailing_comma(self):
        """Test trailing comma is handled."""
        assert parse_comma_separated("headache,nausea,") == ["headache", "nausea"]


class TestGenerateMarkdown:
    """Tests for generate_markdown function."""

    def test_basic_markdown(self):
        """Test basic markdown generation."""
        data = {
            "mood": 1,
            "energy": 7,
            "symptoms": ["headache"],
            "meds": [],
            "tags": [],
            "note": "Test note",
        }
        timestamp = datetime(2025, 10, 30, 21, 37, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        markdown = generate_markdown(data, timestamp)

        assert "---" in markdown
        assert "schema: health-journal/v1" in markdown
        assert "timestamp: '2025-10-30T21:37:00+09:00'" in markdown
        assert "mood: 1" in markdown
        assert "energy: 7" in markdown
        assert "symptoms:" in markdown
        assert "- headache" in markdown
        assert "Test note" in markdown

    def test_markdown_with_meds_and_tags(self):
        """Test markdown with meds and tags."""
        data = {
            "mood": -1,
            "energy": 4,
            "symptoms": ["headache", "nausea"],
            "meds": ["ibuprofen"],
            "tags": ["work"],
            "note": "Test note with meds",
        }
        timestamp = datetime(2025, 10, 30, 21, 37, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        markdown = generate_markdown(data, timestamp)

        assert "meds:" in markdown
        assert "- ibuprofen" in markdown
        assert "tags:" in markdown
        assert "- work" in markdown

    def test_markdown_without_optional_fields(self):
        """Test markdown without optional fields."""
        data = {
            "mood": 0,
            "energy": 5,
            "symptoms": [],
            "meds": [],
            "tags": [],
            "note": "Test note",
        }
        timestamp = datetime(2025, 10, 30, 21, 37, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        markdown = generate_markdown(data, timestamp)

        # meds and tags should not be in output when empty
        assert "meds:" not in markdown
        assert "tags:" not in markdown


class TestGetJournalPath:
    """Tests for get_journal_path function."""

    def test_journal_path_format(self):
        """Test journal path format."""
        timestamp = datetime(2025, 10, 30, 21, 37, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        path = get_journal_path(timestamp, base_dir=Path("journal"))

        assert path == Path("journal/2025/10/2025-10-30T213700+0900.md")

    def test_journal_path_custom_base(self):
        """Test journal path with custom base directory."""
        timestamp = datetime(2025, 10, 30, 21, 37, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        path = get_journal_path(timestamp, base_dir=Path("custom"))

        assert path == Path("custom/2025/10/2025-10-30T213700+0900.md")


class TestSaveJournal:
    """Tests for save_journal function."""

    def test_save_journal(self, tmp_path):
        """Test saving journal to file."""
        markdown = "---\ntest: content\n---\nTest body"
        journal_path = tmp_path / "test.md"

        with patch("builtins.print"):
            save_journal(markdown, journal_path)

        assert journal_path.exists()
        assert journal_path.read_text(encoding="utf-8") == markdown

    def test_save_journal_creates_directory(self, tmp_path):
        """Test saving journal creates parent directories."""
        markdown = "---\ntest: content\n---\nTest body"
        journal_path = tmp_path / "2025" / "10" / "test.md"

        with patch("builtins.print"):
            save_journal(markdown, journal_path)

        assert journal_path.exists()
        assert journal_path.read_text(encoding="utf-8") == markdown


class TestGetInteractiveInput:
    """Tests for get_interactive_input function."""

    @patch("builtins.input")
    @patch("builtins.print")
    def test_interactive_input_valid(self, mock_print, mock_input):
        """Test interactive input with valid values."""
        mock_input.side_effect = [
            "1",  # mood
            "7",  # energy
            "headache",  # symptoms
            "ibuprofen",  # meds
            "work",  # tags
            "Test note",  # note line 1
            "",  # note end
        ]

        result = get_interactive_input()

        assert result["mood"] == 1
        assert result["energy"] == 7
        assert result["symptoms"] == ["headache"]
        assert result["meds"] == ["ibuprofen"]
        assert result["tags"] == ["work"]
        assert result["note"] == "Test note"

    @patch("builtins.input")
    @patch("builtins.print")
    def test_interactive_input_retry_mood(self, mock_print, mock_input):
        """Test interactive input retries on invalid mood."""
        mock_input.side_effect = [
            "5",  # invalid mood
            "1",  # valid mood
            "7",  # energy
            "",  # symptoms
            "",  # meds
            "",  # tags
            "Test",  # note
            "",  # note end
        ]

        result = get_interactive_input()

        assert result["mood"] == 1

    @patch("builtins.input")
    @patch("builtins.print")
    def test_interactive_input_retry_energy(self, mock_print, mock_input):
        """Test interactive input retries on invalid energy."""
        mock_input.side_effect = [
            "1",  # mood
            "15",  # invalid energy
            "7",  # valid energy
            "",  # symptoms
            "",  # meds
            "",  # tags
            "Test",  # note
            "",  # note end
        ]

        result = get_interactive_input()

        assert result["energy"] == 7


class TestCmdWellnessLog:
    """Tests for cmd_wellness_log command."""

    @patch("health_journal.cli.save_journal")
    @patch("health_journal.cli.datetime")
    def test_non_interactive_mode(self, mock_datetime, mock_save):
        """Test non-interactive mode."""
        # Setup
        mock_timestamp = datetime(2025, 10, 30, 21, 37, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        mock_datetime.now.return_value = mock_timestamp

        args = argparse.Namespace(
            mood=1,
            energy=7,
            symptoms="headache",
            meds="ibuprofen",
            tags="work",
            note="Test note",
            dry_run=False,
        )

        # Execute
        result = cmd_wellness_log(args)

        # Verify
        assert result == 0
        assert mock_save.called
        saved_markdown = mock_save.call_args[0][0]
        assert "mood: 1" in saved_markdown
        assert "energy: 7" in saved_markdown
        assert "headache" in saved_markdown

    @patch("health_journal.cli.datetime")
    @patch("builtins.print")
    def test_dry_run_mode(self, mock_print, mock_datetime):
        """Test dry-run mode does not save."""
        # Setup
        mock_timestamp = datetime(2025, 10, 30, 21, 37, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        mock_datetime.now.return_value = mock_timestamp

        args = argparse.Namespace(
            mood=1,
            energy=7,
            symptoms="headache",
            meds="",
            tags="",
            note="Test note",
            dry_run=True,
        )

        # Execute
        result = cmd_wellness_log(args)

        # Verify
        assert result == 0
        # Check that output was printed
        assert mock_print.called

    @patch("health_journal.cli.get_interactive_input")
    @patch("health_journal.cli.save_journal")
    @patch("health_journal.cli.datetime")
    def test_interactive_mode(self, mock_datetime, mock_save, mock_input):
        """Test interactive mode."""
        # Setup
        mock_timestamp = datetime(2025, 10, 30, 21, 37, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
        mock_datetime.now.return_value = mock_timestamp
        mock_input.return_value = {
            "mood": 1,
            "energy": 7,
            "symptoms": ["headache"],
            "meds": [],
            "tags": [],
            "note": "Test note",
        }

        args = argparse.Namespace(
            mood=None,
            energy=None,
            symptoms=None,
            meds=None,
            tags=None,
            note=None,
            dry_run=False,
        )

        # Execute
        result = cmd_wellness_log(args)

        # Verify
        assert result == 0
        assert mock_save.called

    def test_invalid_mood_in_args(self):
        """Test invalid mood in arguments returns error."""
        args = argparse.Namespace(
            mood=5,  # invalid
            energy=7,
            symptoms="",
            meds="",
            tags="",
            note="",
            dry_run=False,
        )

        result = cmd_wellness_log(args)

        assert result == 1

    def test_invalid_energy_in_args(self):
        """Test invalid energy in arguments returns error."""
        args = argparse.Namespace(
            mood=1,
            energy=15,  # invalid
            symptoms="",
            meds="",
            tags="",
            note="",
            dry_run=False,
        )

        result = cmd_wellness_log(args)

        assert result == 1
