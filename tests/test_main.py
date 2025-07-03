"""
Tests for the main module.
"""

import pytest
from src.app import __version__


def test_version():
    """Test that the version is a string."""
    assert isinstance(__version__, str)
    assert __version__ == "0.1.0" 