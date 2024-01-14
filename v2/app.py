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

    # Convert results to list of MaigretSite objects
    results = [MaigretSite.from_dict(result) for result in results]

    # Format results for JSON response
    formatted_results = [{"site": result.site, "status": result.status, "url": result.url} for result in results]

    return jsonify(formatted_results)

if __name__ == "__main__":
    app.run(debug=True)
