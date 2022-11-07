from flask_wtf import FlaskForm
from wtforms import (
    IntegerField, StringField, SubmitField)


class CharacterForm(FlaskForm):

    id = IntegerField("Identificador")
    name = StringField("Nome do Personagem")
    submit = SubmitField("Cadastrar")
