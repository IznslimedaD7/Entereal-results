from flask import Flask
from config import Config
from app.extentions import db, login_manager
from flask_migrate import Migrate
from app.models.user import User
from app.models.LikeToNomination import LikeToNomination
from app.models.nomination import Nomination
from app.models.role import Role

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    Migrate(app, db)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.nomination import bp as nomination_bp
    app.register_blueprint(nomination_bp)

    @app.route('/test')
    def hello():
        return "Hello World!"
    
    return app