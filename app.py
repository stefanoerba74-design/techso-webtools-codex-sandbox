from flask import Flask, render_template

from config import Config
from extensions import db, migrate
from tools.tools_registry import TOOLS_REGISTRY, TOOL_ROADMAP
from apps.earth_grid import create_blueprint as create_earth_grid
from apps.flare_struct import create_blueprint as create_flare_struct
from apps.site_data import create_blueprint as create_site_data
from apps.inst_manager import create_blueprint as create_inst_manager
from apps.inst_manager import models as inst_models  # noqa: F401


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(create_earth_grid())
    app.register_blueprint(create_flare_struct())
    app.register_blueprint(create_site_data())
    app.register_blueprint(create_inst_manager())

    @app.route("/")
    def home():
        return render_template("home.html", tools=TOOLS_REGISTRY)

    @app.route("/tools")
    def tools_list():
        return render_template("tools_list.html", tools=TOOLS_REGISTRY)

    @app.route("/tools/<slug>")
    def tool_detail(slug: str):
        tool = next((item for item in TOOLS_REGISTRY if item["slug"] == slug), None)
        return render_template("tool_detail.html", tool=tool)

    @app.route("/roadmap")
    def roadmap():
        return render_template("roadmap.html", roadmap=TOOL_ROADMAP)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
