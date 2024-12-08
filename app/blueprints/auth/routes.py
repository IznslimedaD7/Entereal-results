from app.blueprints.auth import bp
from app.controllers.authController import AuthController


@bp.route('/registration', methods=["GET"])
def registation():
    return AuthController.registration()

@bp.route('/create/user', methods=["POST"])
def create():
    return AuthController.create()

@bp.route('/login', methods=["GET"])
def login():
    return AuthController.login()

@bp.route('/auth', methods=['POST'])
def auth():
    return AuthController.auth()

@bp.route('/logout')
def logout():
    return AuthController.logout()