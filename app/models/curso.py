from app import db
from sqlalchemy_serializer import SerializerMixin

class Curso(db.Model, SerializerMixin):
    # Este campo se usa si quieren dar un nombre diferente a la tabla (migración)
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    nombre_curso = db.Column(db.String(120), index=True, unique=True)
    descripcion_curso = db.Column(db.String(120), index=True, unique=True)
    frase_curso = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return f'<Curso {self.nombre_curso}>'

    def __name__(self):
        return 'Curso'
