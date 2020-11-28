from app import api, docs
from app.resources.auth_resource import LoginApi, SignupApi
from app.resources.test_resource import TestApi
from app.resources.curso_resource import CursoApi

def initialize_routes(api_rest, doc_rest):
    # Registro
    api_rest.add_resource(SignupApi, '/api/auth/signup')
    doc_rest.register(SignupApi)
    # Login
    api_rest.add_resource(LoginApi, '/api/auth/login')
    # Test [Required token]
    api_rest.add_resource(TestApi, '/api/test')

    # Curso
    api_rest.add_resource(CursoApi, '/api/cursos')
    doc_rest.register(CursoApi)


initialize_routes(api, docs)
