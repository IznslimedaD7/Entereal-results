from app.extentions import db
from app.models.role import Role


def create_roles():
    role_user = Role(title='user')
    role_admin = Role(title='admin')

    db.session.add(role_user)
    db.session.commit()
    db.session.add(role_admin)
    db.session.commit()