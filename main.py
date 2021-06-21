import codecs

import click
from flask import Flask, render_template, request

app = Flask(__name__)


def rot13(s: str) -> str:
    """ROT-13 encode a string.
    This is not a useful thing to do, but serves as an example of a
    transformation that we might apply."""
    return codecs.encode(s, "rot_13")


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    result = rot13(request.form.get("cleartext", ""))
    return render_template("index.html", result=result)


@click.command()
@click.option("-p", "--port", type=int, default=8080)
def main(port):
    """Run the app in debug mode for local testing.
    This function is not invoked in App Engine.
    """
    app.run(port=port, debug=True)


if __name__ == "__main__":
    main()
