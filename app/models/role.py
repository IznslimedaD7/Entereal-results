from app.extentions import db

class Role(db.Model):
    __tablename__ = 'roles'

    _role_admin = 2
    _role_user = 1

    @property
    def role_admin(self):
        return type(self)._role_admin
    
    @property
    def role_user(self):
        return type(self)._role_user
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    users = db.relationship('User', backref='role')

    def __repr__(self) -> str:
        return '<Role %r>' % self.id