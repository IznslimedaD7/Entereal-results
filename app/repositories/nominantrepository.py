from app.extentions import db
from app.models.nominant import Nominat


class NominantsRepository():
    def nominants_by_the_nomination(id):
        return Nominat.query.filter_by(nomination_id=id).all()
    
    def nominant_create(nomination_id, user_id, title):
        nominant = Nominat(nomination_id=nomination_id, user_id=user_id, title=title)
        try:
            db.session.add(nominant)
            db.session.commit()
        except Exception as e:
            db.session.rollback()