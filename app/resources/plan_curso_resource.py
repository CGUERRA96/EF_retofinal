from flask import make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from app.models.curso import Curso
from app.models.plan_curso import Plan_curso

# Necesita en Header Bearer: Token (Este es token generado en el login)
class Plan_CursoResponseSchema(Schema):
    message = fields.Str(default='Contenido del Curso')
    data = []

class Plan_CursoApi(MethodResource,Resource):
    @doc(description='API Plan_Curso.', tags=['Contenido del Curso'])
    @marshal_with(Plan_CursoResponseSchema)
    #@jwt_required # proteger a la vista
    def get(self):
        try:
            plan = Plan_curso.query.all()
            contenido = []

            for i in plan:
                curso = Curso.query.filter_by(id=i.curso_id).first()
                contenido.append({
                    'id': i.id,
                    'curso_id': i.curso_id,
                    'curso': {
                        'name': curso.nombre_curso
                    },
                    'unidad_curso': i.unidad_curso,
                    'periodo_unidad': i.periodo_unidad,
                    'tema_periodo': i.tema_periodo,
                    'contenido_tema': i.contenido_tema
                })

            return make_response(jsonify({
                'message': 'Contenido del Curso',
                'data': contenido
            }), 200)
        except Exception as e:
            print(e)
            return make_response(jsonify({
                'message': 'Ocurrio un error'
            }), 500)

#crear un metodo donde 