from flask import make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required


# Necesita en Header Bearer: Token (Este es token generado en el login)
class TestApi(Resource):
    @jwt_required
    def get(self):
        return make_response(jsonify({
            'message': 'Test'
        }), 500)