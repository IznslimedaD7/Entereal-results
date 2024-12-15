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

@bp.route('/nomination/<int:id>/nominants')
def nominants(id):
    return NominationController.nominants(id)

@bp.route('/nomination/<int:id>/nominant/create', methods=["POST"])
def create_nominant(id):
    return NominationController.create_nominant(id)

@bp.route('/nomination/<int:id>/edit')
def edit(id):
    return NominationController.edit(id)

@bp.route('/nomination/<int:id>/store_edit', methods=["POST"])
def store_edit(id):
    return NominationController.store_edit(id)