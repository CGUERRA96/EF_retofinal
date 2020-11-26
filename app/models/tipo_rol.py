from app import db

class Tipo_rol(db.Model):
    # Este campo se usa si quieren dar un nombre diferente a la tabla (migración)
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    tiporol = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return f'<TipoRol {self.tiporol}>'

    def __name__(self):
        return 'Tipo_Rol'