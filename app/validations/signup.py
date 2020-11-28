from kanpai.Kanpai import Object, Email, String

schema = Object({
    'nombres': (String(error='Debe ser un campo string')).trim().required(error='Se necesita el campo nombres'),
    'apellidos': (String(error='Debe ser un campo string')).trim().required(error='Se necesita el campo apellidos'),
    'email': (Email(error='No es un correo valido')).trim().required(error='Se necesita el campo email'),
    'celular': (String(error='No es un número correcto')).trim().required(error='Se necesita el campo celular'),
    'username': (String(error='Debe ser un campo string')).trim().required(error='Se necesita el campo username'),
    'password': (String(error='Debe ser un campo string')).trim().required(error='Se necesita el campo password')
})


def validation(payload):
    validation_result = schema.validate(payload)
    return validation_result
