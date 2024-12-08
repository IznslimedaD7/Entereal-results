from app.extentions import db
from app.models.user import User
from werkzeug.security import generate_password_hash


class AuthRepository():
    def registration(login, nickname, password, role_id):
        user = User(login=login, nickname=nickname, password_hash=generate_password_hash(password), role_id=role_id)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
        return user
    
    def auth(login):
        return db.session.query(User).filter(User.login == login).first()
