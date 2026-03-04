from flask import Blueprint, render_template

bp = Blueprint("about", __name__)

@bp.route("/about")
def main():
    return render_template("about.html")