from flask import Blueprint, render_template

from .models import Instrument


def register() -> Blueprint:
    bp = Blueprint("inst_manager", __name__, url_prefix="/inst-manager")

    @bp.route("/")
    def dashboard():
        return render_template("inst_manager/dashboard.html")

    @bp.route("/instruments")
    def instruments():
        items = Instrument.query.order_by(Instrument.tag.asc()).all()
        return render_template("inst_manager/instruments.html", instruments=items)

    return bp
