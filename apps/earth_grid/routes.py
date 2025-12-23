from flask import Blueprint, render_template


def register() -> Blueprint:
    bp = Blueprint("earth_grid", __name__, url_prefix="/earth-grid")

    @bp.route("/")
    def dashboard():
        return render_template("earth_grid/dashboard.html")

    return bp
