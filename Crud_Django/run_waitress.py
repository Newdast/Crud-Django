from whitenoise import WhiteNoise
from Crud_Django.wsgi import application

# Crea una instancia de WhiteNoise
application = WhiteNoise(application)

if __name__ == "__main__":
    from waitress import serve
    serve(application, host='0.0.0.0', port=8000)
