#!/usr/bin/env python3

import sys
import argparse
import logging

from flaskquotes import afi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--rank', type=int)
    args = parser.parse_args()

    if not afi.check_json_exists():
        build_quotes_file()

    quotes = afi.fetch_quotes_json()
    top100 = afi.AFITop100(quotes)

    if args.rank is not None:
        rank, quote = top100.get_quote(args.rank)
    else:
        rank, quote = top100.get_random_quote()

    formatted = f"#{rank} {quote['Quote']} - from {quote['Movie']} ({quote['Year']})"
    print(formatted)
    sys.exit()


def build_quotes_file():
    try:
        source = afi.fetch_afi_quotes_html()
        if source is None:
            logging.error(f"Failed to fetch quotes from afi.com.")
    except RuntimeError as e:
        logging.error(f"Quotes are unavailable: {e}")
        raise

    quotes = afi.find_quotes(source)
    packed_quotes = afi.pack_quotes(quotes, quotetag='h6.q_title', movietag='a.movie-detail')
    afi.store_quotes_json(packed_quotes)


if __name__ == '__main__':
    main()
