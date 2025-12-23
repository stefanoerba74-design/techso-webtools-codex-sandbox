from flask import Blueprint, render_template


def register() -> Blueprint:
    bp = Blueprint("site_data", __name__, url_prefix="/site-data")

    @bp.route("/")
    def dashboard():
        return render_template("site_data/dashboard.html")

    return bp
