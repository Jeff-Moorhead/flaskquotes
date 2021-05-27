import requests
import json
import os
import logging

from random import randint
from bs4 import BeautifulSoup


class AFITop100:
    def __init__(self, quotes):
        self.quotes = quotes

    def get_random_quote(self):
        firstquote_index = min(self.quotes.keys())
        lastquote_index = max(self.quotes.keys())
        random_index = randint(firstquote_index, lastquote_index)
        return tuple([random_index, self.quotes[random_index]])

    def get_quote(self, index):
        return tuple([index, self.quotes.get(index)])


def store_quotes_json(packed_quotes):
    quotes_file = get_quotes_filename()

    if not os.path.exists(os.path.dirname(quotes_file)):
        os.makedirs(os.path.dirname(quotes_file))

    with open(quotes_file, 'w') as fh:
        json.dump(packed_quotes, fh)


def fetch_quotes_json():
    quotes_file = get_quotes_filename()

    with open(quotes_file, 'r') as fh:
        quotes = json.load(fh)

    keys = map(int, quotes.keys())

    return dict(zip(keys, quotes.values()))


def check_json_exists():
    quotes_file = get_quotes_filename()
    return os.path.exists(quotes_file)


def get_quotes_filename():
    datadir = os.path.expandvars("$HOME/data")
    return os.path.join(datadir, 'quotes.json')


def fetch_afi_quotes_html(url='https://www.afi.com/afis-100-years-100-movie-quotes/'):
    try:
        page = requests.get(url)
        page.raise_for_status()
        return page.content
    except requests.exceptions.HTTPError as e:
        logging.error(f"Something went wront in fetch_afi_quotes_html: {e}")
        raise
    except requests.ConnectionError as e:
        logging.error("No internet connection available to fetch quotes.")
        raise 


def find_quotes(html, selector='div.single_list.col-sm-12.movie_popup'):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        quotes = soup.select(selector)
        return quotes
    except Exception as e:
        logging.error(f"Unable to select movie elements: {e}")
        raise


def pack_quotes(quotes, **kwargs):
    """
    :param quotes: a list of BeautifulSoup tags containing quotes, and quote details
    :return: a dictionary of packaged quotes
    """
    packed_quotes = {}

    for group in quotes:
        raw = group.select_one(kwargs.get('quotetag'))
        raw_quote = raw.string
        raw_quote = raw_quote.strip()
        rank, quote = raw_quote.split(" ", 1)
        rank = int(rank.rstrip("."))

        raw = group.select_one(kwargs.get('movietag'))
        raw_movie, raw_year = raw.strings
        raw_movie = raw_movie.strip()
        movie = raw_movie.title()
        raw_year = raw_year.lstrip('(')
        year = raw_year.rstrip(')')

        packed_quotes[rank] = {"Quote": quote, "Movie": movie, "Year": year}

    return packed_quotes
