from flask import Blueprint, current_app, render_template, jsonify

competency_bp = Blueprint("competency", __name__)


@competency_bp.get("/")
def index():
    service = current_app.extensions["services"]["competency"]
    profile = service.get_profile()
    return render_template("pages/competency.html", profile=profile, active_page="competency")

@competency_bp.get("/api/profile")
def profile_api():
    service = current_app.extensions["services"]["competency"]
    return jsonify(service.get_profile())