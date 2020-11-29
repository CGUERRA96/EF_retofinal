from flask import make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from app.models.curso import Curso
from app.models.categoria import Categoria
from app.models.oferta_curso import Oferta_curso

# Necesita en Header Bearer: Token (Este es token generado en el login)
class Oferta_CursoResponseSchema(Schema):
    message = fields.Str(default='Listado de Cursos Ofertados')
    data = []

class Oferta_CursoApi(MethodResource,Resource):
    @doc(description='API Oferta_Curso.', tags=['Lista_Oferta'])
    @marshal_with(Oferta_CursoResponseSchema)
    #@jwt_required # proteger a la vista
    def get(self):
        try:
            oferta = Oferta_curso.query.all()
            lista = []

            for i in oferta:
                curso = Curso.query.filter_by(id=i.curso_id).first()
                lista.append({
                    'id': i.id,
                    'curso_id': i.curso_id,
                    'curso': {
                        'name': curso.nombre_curso
                    },
                    'fechainicio': i.fechainicio,
                    'fechafin': i.fechafin,
                    'tema_periodo': i.tema_periodo,
                    'contenido_tema': i.contenido_tema
                })

            return make_response(jsonify({
                'message': 'Listado de Curso Ofertados',
                'data': lista
            }), 200)
        except Exception as e:
            print(e)
            return make_response(jsonify({
                'message': 'Ocurrio un error'
            }), 500)

#crear un metodo donde 