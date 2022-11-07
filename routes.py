from flask import render_template

from character import character_blueprint
from character.forms import CharacterForm

from main import db
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

    if character_form.validate_on_submit():
        character = Character(
            id=character_form.id.data,
            name=character_form.name.data)

        db.session.add(character)

        db.session.commit()

        return "Personagem registrado com sucesso", 200

    return render_template("character/new.html", form=character_form)
