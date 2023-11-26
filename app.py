from flask import Flask, request, render_template
import asyncio
import logging
from maigretsearch import perform_maigret_search


# Initialize Flask app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get username from form
        username = request.form.get("username")

        # Perform Maigret search
        results = perform_maigret_search(username)

        # Render results template
        return render_template("results.html", results=results)

    # Render index template
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
