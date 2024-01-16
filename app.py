<<<<<<< HEAD
from flask import Flask, request, render_template, abort
import logging
from maigretsearch import perform_maigret_search

app = Flask(__name__)

def configure_logging():
    logging.basicConfig(level=logging.INFO)

def load_configuration(app):
    # Load configuration from environment variables or configuration file
    app.config.from_pyfile('config.py', silent=True)

def validate_username(username):
    if not username:
        logging.error("No username provided")
        abort(400, description="No username provided")
    return username

async def perform_search(username):
    return await perform_maigret_search(username)

def configure_routes(app):
    @app.route("/", methods=["GET", "POST"])
    async def index():
        try:
            if request.method == "POST":
                username = validate_username(request.form.get("username"))
                results = await perform_search(username)
                logging.info(f"Search performed for username: {username}")
                return render_template("results.html", results=results)

            return render_template("index.html")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            abort(500, description="Internal Server Error")

def main():
    configure_logging()
    load_configuration(app)
    configure_routes(app)
    app.run(debug=app.config.get('DEBUG', False), use_reloader=True)

if __name__ == "__main__":
    main()
=======
from flask import Flask, request, jsonify
import asyncio
from maigret.maigret import maigret as maigret_search
from maigret.sites import MaigretSite
from gretlogger import setup_logger

app = Flask(__name__)

async def async_maigret_search(username, information, logger):
    """Asynchronously perform a search using Maigret."""
    site = MaigretSite(username, information)
    return await maigret_search(username, information, logger)

@app.route("/search", methods=["POST"])
def search():
    """Endpoint to perform username search."""
    data = request.get_json()
    username = data.get("username")

    # Set up logger
    logging = data.get("logging")
    logger = setup_logger("maigret", level=logging.DEBUG)

    # Set up information
    information = data.get("information")  # Define the "information" variable

    # Performing the search asynchronously
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(async_maigret_search(username, information, logger))
    loop.close()

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> eae0de0bcbddcb1a2ef02e536cf06b50e10f8ee2
