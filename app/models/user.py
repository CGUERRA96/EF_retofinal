from app import db

class User(db.Model):
    # Este campo se usa si quieren dar un nombre diferente a la tabla (migración)
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'))
    tipo_rol_id = db.Column(db.Integer, db.ForeignKey('tipo_rol.id'))

    def __repr__(self):
        return f'<User {self.id}>'

    def __name__(self):
        return 'User'
