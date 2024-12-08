from app.blueprints.nomination import bp
from app.controllers.nominationController import NominationController


@bp.route('/nominations')
def index():
    return NominationController.nominations()

@bp.route('/nomination/create')
def create():
    return NominationController.create()

@bp.route('/nomination/store', methods=["POST"])
def store():
    return NominationController.store()

@bp.route('/nomination/<int:id>/like/add', methods=["POST"])
def add_like(id):
    return NominationController.add_like(id)

@bp.route('/nomination/<int:id>/like/remove', methods=["POST"])
def remove_like(id):
    return NominationController.remove_like(id)