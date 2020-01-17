#!/usr/bin/env python3

import sys
import argparse

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
    sys.exit()


def build_quotes_file():
    try:
        source = afi.fetch_afi_quotes_html()
        if source is None:
            print('Quotes is currently unavailable. Please try again later')
            sys.exit()
    except RuntimeError:
        print('Quotes are unavailable. Please connect to the internet and try again.')
        sys.exit()

    quotes = afi.find_quotes(source)
    packed_quotes = afi.pack_quotes(quotes, quotetag='h6.q_title', movietag='a.movie-detail')
    afi.store_quotes_json(packed_quotes)


if __name__ == '__main__':
    main()
