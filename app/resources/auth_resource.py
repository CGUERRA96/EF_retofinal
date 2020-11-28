from app import db
from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
#from app.models.user import User
from app.models.persona import Persona
from flask_jwt_extended import create_access_token
from datetime import timedelta
from app.validations.login import validation as validate_login
from app.validations.signup import validation as validate_signup


class SignupResponseSchema(Schema):
    message = fields.Str(default='Usuario creado con exito')
    persona_id = fields.Integer()


class SignupRequestSchema(Schema):
    nombres = fields.Str(required=True)
    apellidos = fields.Str(required=True)
    email = fields.Str(required=True)
    celular = fields.Integer(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class SignupApi(MethodResource, Resource):
    @doc(description='API Registro.', tags=['Auth'])
    @use_kwargs(SignupRequestSchema, location=('json'))
    @marshal_with(SignupResponseSchema)
    def post(self, **kwargs):
        try:
            # Validación
            validation_result = validate_signup(request.json)
            if validation_result.get('success', False) is False:
                return make_response(jsonify({
                    'errors': validation_result.get("error")
                }), 500)

            # Creación del usuario
            body = request.get_json()
            persona_model = Persona(**body)
            persona_model.hash_password()
            db.session.add(persona_model)
            db.session.commit()
            persona_id = persona_model.id

            # Retorno de datos del usuario
            return make_response(jsonify({
                'message': 'Usuario creado con exito',
                'persona_id': persona_id
            }), 201)
        except Exception as e:
            # Error
            return make_response(jsonify({
                'message': 'Ocurrio un error'
            }), 500)


class LoginApi(Resource):
    def post(self):
        try:
            # Validación
            validation_result = validate_login(request.json)
            if validation_result.get('success', False) is False:
                return make_response(jsonify({
                    'errors': validation_result.get("error")
                }), 500)

            # Busqueda del usuario
            body = request.get_json()
            persona = Persona.query.filter_by(email=body.get('email')).first()
            authorized = persona.check_password(body.get('password'))
            if not authorized:
                return make_response(jsonify({
                    'message': 'Credenciales Erroneas'
                }))

            # Retorno y creación del token
            expires = timedelta(days=7)
            access_token = create_access_token(identity=str(persona.id), expires_delta=expires)
            return make_response(jsonify({
                'token': access_token
            }), 200)
        except Exception as e:
            print(e)
            # Error
            return make_response(jsonify({
                'message': 'Ocurrio un error'
            }), 500)
