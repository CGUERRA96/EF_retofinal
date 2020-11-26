from kanpai.Kanpai import Object, Email, String

schema = Object({
    'username': (String(error='Debe ser un campo string')).trim().required(error='Se necesita el campo username'),
    'email': (Email(error='No es un correo valido')).trim().required(error='Se necesita el campo email'),
    'password': (String(error='Debe ser un campo string')).trim().required(error='Se necesita el campo password')
})


def validation(payload):
    validation_result = schema.validate(payload)
    return validation_result
