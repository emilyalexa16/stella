from flask import Blueprint, redirect, render_template, url_for, session
from ..services.save_service import load_save_file
from ..services.friendship_service import get_friendship_focus
from ..services.skills_service import get_skill_focus
from ..services.progression_service import get_progression_focus

bp = Blueprint("categories", __name__)

@bp.route('/verify_session')
def verify_session():
    if "uploaded_file" not in session:
        return redirect(url_for("main.index"))

    return render_template("options.html")

@bp.route("/friendships", methods=["GET"])
def friendships():
    uploaded_file = session.get('uploaded_file')
    data = load_save_file(uploaded_file)
    friend = get_friendship_focus(data)
    return render_template("friendships.html", friend=friend)

@bp.route("/skills", methods=["GET"])
def skills():
    uploaded_file = session.get('uploaded_file')
    data = load_save_file(uploaded_file)
    skill = get_skill_focus(data)
    return render_template("skills.html", skill=skill)

@bp.route("/progression", methods=["GET"])
def progression():
    uploaded_file = session.get('uploaded_file')
    data = load_save_file(uploaded_file)
    milestone = get_progression_focus(data)
    return render_template("progression.html", milestone=milestone)