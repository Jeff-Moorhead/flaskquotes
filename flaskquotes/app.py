#!/usr/bin/env python3

import flask
import logging

from flaskquotes import afi, console

app = flask.Flask(__name__)


@app.route('/')
def quote():
    if not afi.check_json_exists():
        try:
            console.build_quotes_file()
        except Exception as e:
            logging.error(f"Unable to build quotes file: {e}")
            raise 

    try:
        quotes = afi.fetch_quotes_json()
        return flask.render_template('index.html', quotes=quotes)
    except Exception as e: 
        logging.error(f"Unable to render index.html: {e}")
        raise

def get_quote():
    if not afi.check_json_exists():
        afi.build_quotes_file()

    quotes = afi.fetch_quotes_json()
    top100 = afi.AFITop100(quotes)

    return top100.get_random_quote()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run()
