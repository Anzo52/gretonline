from flask import Flask, request, render_template
from maigret import MaigretSite, MaigretDatabase, search as maigret_search
from gretlogger import setup_logger

app = Flask(__name__)


@app.route("/search", methods=["GET", "POST"])
async def search_route():
    if request.method != "POST":
        # For a GET request, just display the search form
        return render_template("search_form.html")
    # Extract data from the form
    username = request.form["username"]
    # Perform search with Maigret here
    results = await perform_maigret_search(username)
    return render_template("results.html", results=results)


async def perform_maigret_search(username):
    logger = setup_logger(__name__)
    # Initialize Maigret database
    maigret_sites_file = "./env/lib/python3.9/site-packages/maigret/resources/data.json"
    db = MaigretDatabase().load_from_file(maigret_sites_file)

    # Perform the search
    try:
        result = await maigret_search(username, db, logger)
        # Format and return the results
        return format_maigret_results(result)
    except Exception as e:
        logger.error(f"Error while searching for {username}: {e}")
        return None


def format_maigret_results(results):
    return {
        site_name: data["url_user"]
        for site_name, data in results.items()
        if data["exists"]
    }


if __name__ == "__main__":
    app.run(debug=True)
