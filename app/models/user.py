from app.extentions import db
from flask_login import UserMixin
from app.extentions import login_manager
from app.models.role import Role


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)
    
    nominations = db.relationship('Nomination', backref='user', lazy=True)
    liked_nominations = db.relationship('LikeToNomination', back_populates='user', lazy=True)

    def __repr__(self) -> str:
        return '<User %r>' % self.id
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)