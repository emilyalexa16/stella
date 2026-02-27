from flask import Blueprint, render_template
from ..services.save_service import load_save_file
from ..services.friendship_service import get_friendship_focus
from ..services.skills_service import get_skill_focus
from ..services.progression_service import get_progression_focus

bp = Blueprint("stella", __name__)

SAVE_PATH = "/Users/emilygotiangco/.config/StardewValley/Saves/Stella_430626840/Stella_430626840"
#SAVE_PATH = "/Users/emilygotiangco/School/cmps_490/Saves/Ivans_401983009/Ivans_401983009"

@bp.route("/friendships", methods=["GET"])
def friendships():
    data = load_save_file(SAVE_PATH)
    friend = get_friendship_focus(data)
    return render_template("friendships.html", friend=friend)

@bp.route("/skills", methods=["GET"])
def skills():
    data = load_save_file(SAVE_PATH)
    skill = get_skill_focus(data)
    return render_template("skills.html", skill=skill)

@bp.route("/progression", methods=["GET"])
def progression():
    data = load_save_file(SAVE_PATH)
    milestone = get_progression_focus(data)
    return render_template("progression.html", milestone=milestone)