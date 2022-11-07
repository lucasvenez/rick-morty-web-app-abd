from flask import render_template

from character import character_blueprint
from character.forms import CharacterForm

from model import Character


@character_blueprint.route("/", methods=["GET"])
def list_characters():
    characters = Character.query.all()
    return render_template(
        "character/list.html",
        characters=characters
    )


@character_blueprint.route("/new", methods=["GET", "POST"])
def new_character():
    character_form = CharacterForm()
    return render_template("character/new.html", form=character_form)
