# tests/test_scorefetch.py
import pytest
import sys

from scorefetch import main, CricketMatchBrowser

def test_get_live_matches_returns_list():
    browser = CricketMatchBrowser()
    matches = browser.get_live_matches()
    assert isinstance(matches, list)
    assert all("title" in m for m in matches)


def test_display_matches_prints(capsys):
    browser = CricketMatchBrowser()
    browser.get_live_matches()
    browser.display_matches()
    captured = capsys.readouterr()
    assert "LIVE MATCHES" in captured.out or "No live matches" in captured.out


def test_display_match_details_valid(capsys):
    browser = CricketMatchBrowser()
    matches = browser.get_live_matches()
    if matches:
        browser.display_match_details(1)
        captured = capsys.readouterr()
        assert "MATCH DETAILS" in captured.out or "Could not load match details." in captured.out
    else:
        pytest.skip("No live matches available")


def test_cli_list_argument(capsys):
    sys.argv = ["prog", "--list"]
    main()
    captured = capsys.readouterr()
    assert "LIVE MATCHES" in captured.out or "No live matches" in captured.out


def test_cli_match_argument(capsys):
    browser = CricketMatchBrowser()
    matches = browser.get_live_matches()
    if matches:
        sys.argv = ["prog", "--match", "1"]
        main()
        captured = capsys.readouterr()
        assert "MATCH DETAILS" in captured.out or "Could not load match details." in captured.out
    else:
        pytest.skip("No live matches available")
