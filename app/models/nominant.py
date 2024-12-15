from app.extentions import db
from app.models.user import User
from app.models.nomination import Nomination


class Nominat(db.Model):
    __tablename__ = 'nominants'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    nomination_id = db.Column(db.Integer, db.ForeignKey(Nomination.id), nullable=False)
    user_id  = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __repr__(self) -> str:
        return '<Nominats %r>' % self.id