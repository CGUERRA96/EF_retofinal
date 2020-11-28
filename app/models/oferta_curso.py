from app import db

class Oferta_curso(db.Model):
    # Este campo se usa si quieren dar un nombre diferente a la tabla (migración)
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'))
    fechainicio = db.Column(db.String(64), index=True, unique=True)
    fechafin = db.Column(db.String(64), index=True, unique=True)
    tema_periodo = db.Column(db.String(64), index=True, unique=True)
    contenido_tema = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return f'<Plan {self.contenido_tema}>'

    def __name__(self):
        return 'Plan'