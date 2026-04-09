from flask import Blueprint, render_template

bp = Blueprint("instructions", __name__)

@bp.route("/instructions")
def main():
    return render_template("instructions.html")