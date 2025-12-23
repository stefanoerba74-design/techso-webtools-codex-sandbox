from flask import Flask

from config import Config
from extensions import init_extensions


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    init_extensions(app)

    @app.get("/")
    def index() -> str:
        return "OK"

    return app


if __name__ == "__main__":
    create_app().run()
