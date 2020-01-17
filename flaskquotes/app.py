import flask
from . import afi 

app = flask.Flask(__name__)


@app.route('/')
def quote():
    rank, quote = get_quote()

    formatted = f"#{rank} - {quote['Quote']} - from {quote['Movie']} ({quote['Year']})"
    twitter = f"https://twitter.com/intent/tweet?text=\"{quote['Quote']}\"%20%20%20&hashtags={quote['Movie']},Python,Flask"

    return flask.render_template('index.html', quote=formatted, link=twitter)
    

def get_quote():
    if not afi.check_json_exists():
        build_quotes_file()

    quotes = afi.fetch_quotes_json()
    top100 = afi.AFITop100(quotes)
    if not afi.check_json_exists():
        build_quotes_file()

    quotes = afi.fetch_quotes_json()
    top100 = afi.AFITop100(quotes)

    return top100.get_random_quote()


if __name__ == '__main__':
    app.run()
