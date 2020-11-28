from app import db

class Categoria(db.Model):
    # Este campo se usa si quieren dar un nombre diferente a la tabla (migración)
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return f'<Categoria {self.categoria}>'

    def __name__(self):
        return 'Categoria'
