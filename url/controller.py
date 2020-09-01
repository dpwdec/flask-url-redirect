from flask import Blueprint

url_controller = Blueprint("blueprint", __name__)


@url_controller.route("/")
def generate():
    return "Generation will happen here."
