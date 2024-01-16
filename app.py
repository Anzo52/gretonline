from flask import Flask, request, render_template, abort
import logging
from maigretsearch import perform_maigret_search  # Ensure this module and function are correctly implemented

# Initialize Flask app
app = Flask(__name__)

def configure_logging():
    logging.basicConfig(level=logging.INFO)

def load_configuration(app):
    # Load configuration from environment variables or configuration file
    app.config.from_pyfile('config.py', silent=True)

@app.route("/", methods=["GET", "POST"])
async def index():
    try:
        if request.method == "POST":
            # Process form data
            username = request.form.get("username")
            if not username:
                logging.error("No username provided")
                abort(400, description="No username provided")

            # Perform search using maigretsearch module
            results = await perform_maigret_search(username)
            logging.info(f"Search performed for username: {username}")

            # Render results template
            return render_template("results.html", results=results)

        # Render index template for GET requests
        return render_template("index.html")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        abort(500, description="Internal Server Error")

def main():
    configure_logging()
    load_configuration(app)
    app.run(debug=app.config.get('DEBUG', False), use_reloader=True)

if __name__ == "__main__":
    main()
