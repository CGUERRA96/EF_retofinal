from app import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
    # Este campo se usa si quieren dar un nombre diferente a la tabla (migración)
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

    def __name__(self):
        return 'User'

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
