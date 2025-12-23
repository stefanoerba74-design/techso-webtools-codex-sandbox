from flask import Blueprint, render_template


def register() -> Blueprint:
    bp = Blueprint("flare_struct", __name__, url_prefix="/flare-struct")

    @bp.route("/")
    def dashboard():
        return render_template("flare_struct/dashboard.html")

    return bp
