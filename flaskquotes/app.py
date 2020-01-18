import flask
from . import afi 

app = flask.Flask(__name__)


@app.route('/')
def quote():
    quotes = afi.fetch_quotes_json()

    return flask.render_template('index.html', quotes=quotes)
    

def get_quote():
    if not afi.check_json_exists():
        afi.build_quotes_file()

    quotes = afi.fetch_quotes_json()
    top100 = afi.AFITop100(quotes)

    return top100.get_random_quote()


if __name__ == '__main__':
    app.run()
