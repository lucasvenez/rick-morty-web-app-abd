from character import character_blueprint

@character_blueprint.route("/", methods=["GET"])
def list_characters():
    pass