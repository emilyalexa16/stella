from flask import Blueprint, render_template

bp = Blueprint("contact", __name__)

@bp.route("/contact")
def main():
    return render_template("contact.html")