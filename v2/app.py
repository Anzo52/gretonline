from flask import Flask, app, request, jsonify
from maigret.checking import maigret as maigret_search
from maigret.sites import MaigretEngine, MaigretSite, MaigretDatabase
from typing import Mapping

app = Flask(__name__)


@app.route("/search", methods=["POST"])
def search():
    username = request.json["username"] if request.json is not None else None
    results = search_username(username)
    return jsonify(results)


def search_username(username):
    maigretengine = MaigretEngine(name="engine_name", data="engine_data")
    maigretsite: Mapping[str, type[MaigretSite]] = {"site_name": MaigretSite}
    maigretdatabase = {"database_name": MaigretDatabase}


if __name__ == "__main__":
    app.run(debug=True)
