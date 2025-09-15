# scorefetch/cli.py
import argparse
from .scorefetch import CricketMatchBrowser

def main():
    parser = argparse.ArgumentParser(description="Cricket CLI Score Tracker")
    parser.add_argument('--list', action='store_true', help='List live matches')
    parser.add_argument('--match', type=int, help='Select match number to view details')
    args = parser.parse_args()

    browser = CricketMatchBrowser()
    browser.get_live_matches()

    if args.list:
        browser.display_matches()
    elif args.match:
        browser.display_match_details(args.match)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
