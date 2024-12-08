from app.extentions import db
from app.models.nomination import Nomination
from app.models.LikeToNomination import LikeToNomination


class  NominationRepository():
    def get_all_nominations():
        return Nomination.query.all()
    
    def create_nomination(title, description, user_id):
        nomination = Nomination(title=title, description=description, user_id=user_id)

        try:
            db.session.add(nomination)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def add_like(nomination_id, user_id):
        like = LikeToNomination(nomination_id=nomination_id, user_id=user_id)
        try:
            db.session.add(like)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def remove_like(nomination_id, user_id):

        like = LikeToNomination.query.filter_by(nomination_id=nomination_id, user_id=user_id).first()
        print(like.id)
        try:
            db.session.delete(like)
            db.session.commit()
        except Exception as e:
            db.session.rollback()