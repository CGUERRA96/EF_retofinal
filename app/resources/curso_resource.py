from flask import make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from app.models.curso import Curso
from app.models.categoria import Categoria

# Necesita en Header Bearer: Token (Este es token generado en el login)
class CursoResponseSchema(Schema):
    message = fields.Str(default='Usuario creado con exito')
    data = []

class CursoApi(MethodResource,Resource):
    @doc(description='API Curso.', tags=['Curso'])
    @marshal_with(CursoResponseSchema)
    #@jwt_required # proteger a la vista
    def get(self):
        try:
            cursos = Curso.query.all()
            lista = []

            for i in cursos:
                categoria = Categoria.query.filter_by(id=i.categoria_id).first()
                lista.append({
                    'id': i.id,
                    'categoria_id': i.categoria_id,
                    'categoria': {
                        'name': categoria.categoria
                    },
                    'nombre_curso': i.nombre_curso,
                    'descripcion_curso': i.descripcion_curso,
                    'frase_curso': i.frase_curso
                })

            return make_response(jsonify({
                'message': 'Listado de Curso',
                'data': lista
            }), 200)
        except Exception as e:
            print(e)
            return make_response(jsonify({
                'message': 'Ocurrio un error'
            }), 500)

#crear un metodo donde 