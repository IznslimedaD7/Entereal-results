from flask import Blueprint

bp = Blueprint('nomination', __name__)

from app.blueprints.nomination import routes