from app.extentions import db


class LikeToNomination(db.Model):
    __tablename__ = 'nomination_like'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer,
                           db.ForeignKey('users.id'))
    nomination_id = db.Column('nomination_id', db.Integer,
                         db.ForeignKey('nominations.id'))

    user = db.relationship("User", back_populates="liked_nominations")
    nomination = db.relationship("Nomination", back_populates="liked_users")
