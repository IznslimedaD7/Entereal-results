from app.extentions import db
from app.models.user import User


class Nomination(db.Model):
    __tablename__ = 'nominations'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id  = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    liked_users = db.relationship('LikeToNomination', back_populates='nomination', lazy=True)

    def __repr__(self) -> str:
        return '<Nomination %r>' % self.id