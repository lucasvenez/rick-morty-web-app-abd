from flask import render_template

from index import index_blueprint


@index_blueprint.route("/", methods=["GET"])
@index_blueprint.route("/index", methods=["GET"])
def index():
    return render_template("index.html")
    