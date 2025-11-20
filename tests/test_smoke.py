"""Smoke tests for health_journal package."""

import subprocess
import sys


def test_import_package():
    """Test that the package can be imported."""
    import health_journal
    assert health_journal.__version__ == "0.1.0"


def test_version_command():
    """Test that `python -m health_journal --version` works."""
    result = subprocess.run(
        [sys.executable, "-m", "health_journal", "--version"],
        capture_output=True,
        text=True,
        check=False
    )
    assert result.returncode == 0
    assert "0.1.0" in result.stdout or "0.1.0" in result.stderr


def test_help_command():
    """Test that `python -m health_journal --help` works."""
    result = subprocess.run(
        [sys.executable, "-m", "health_journal", "--help"],
        capture_output=True,
        text=True,
        check=False
    )
    assert result.returncode == 0
    assert "health_journal" in result.stdout.lower() or "Health Journal" in result.stdout
