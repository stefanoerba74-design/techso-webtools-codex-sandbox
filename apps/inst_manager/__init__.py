from .routes import register


def create_blueprint():
    return register()
