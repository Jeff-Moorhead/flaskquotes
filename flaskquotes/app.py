import flask
from flaskquotes import afi, console

app = flask.Flask(__name__)


@app.route('/')
def quote():
    if not afi.check_json_exists():
        try:
            console.build_quotes_file()
        except Exception as e:
            raise Exception(f"Unable to build quotes file: {e}")

    try:
        quotes = afi.fetch_quotes_json()
        return flask.render_template('index.html', quotes=quotes)
    except Exception as e: 
        raise Exception(f"Unable to get quotes json: {e}")

def get_quote():
    if not afi.check_json_exists():
        afi.build_quotes_file()

    quotes = afi.fetch_quotes_json()
    top100 = afi.AFITop100(quotes)

    return top100.get_random_quote()


if __name__ == '__main__':
    app.run()
