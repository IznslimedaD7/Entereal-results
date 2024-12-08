from app.blueprints.main import bp
from app.controllers.mainController import MainController


@bp.route('/')
def main():
    return MainController.index()