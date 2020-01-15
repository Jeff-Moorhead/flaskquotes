import requests
import json
import os
from bs4 import BeautifulSoup

# 1. Fetch whole webpage
# 2. Parse page for all <div class="row"> where parent is <div class="single_list movie_popup">
# 3. Get the quote from <div class="m_head"><h6>
# 4. Get the movie title from <a class="movie-detail">
# 5. Get extra movie data from <div class="col-sm-6"><p>...
# 6. Package all data and store. Provide function to access random quote from data.


class AFITop100:
    def __init__(self, html):
        quotetags = find_quotes(html)
        self.quotes = pack_quotes(quotetags)

    def get_random_quote(self):
        pass


def fetch_afi_quotes_html(url='https://www.afi.com/afis-100-years-100-movie-quotes/'):
    page = requests.get(url)    
    page.raise_for_status()
    return page


def find_quotes(html, selector='div.single_list.col-sm-12.movie_popup'):
    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.select(selector)
    return quotes


def pack_quotes(quotes, **kwargs):
    """
    :param quotes: a list of BeautifulSoup tags containing quotes, and quote details
    :return: a dictionary of packaged quotes
    """
    packed_quotes = {}
    for group in quotes:
        raw = group.select_one(kwargs['quote'])
        raw_quote = raw.string
        raw_quote = raw_quote.strip()
        rank, quote = raw_quote.split(" ", 1)
        rank = rank.rstrip(".")

        raw = group.select_one(kwargs['movie'])
        raw_movie, raw_year = raw.strings
        raw_movie = raw_movie.strip()
        movie = raw_movie.title()
        raw_year = raw_year.lstrip('(')
        year = raw_year.rstrip(')')

        packed_quotes[rank] = {"Quote": quote, "Movie": movie, "Year": year}
    return packed_quotes


def store_json(packed_quotes):
    currdir, currfile = os.path.split(__file__)
    if os.path.exists(os.path.join(currdir, 'data/quotes.json')):
        return
    else:
        with open(os.path.join(currdir, 'data/quotes.json'), 'w') as fh:
            json.dump(packed_quotes, fh)
