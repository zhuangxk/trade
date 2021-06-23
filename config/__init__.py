from app import app
import config.default
import config.prod
import os

FLASK_ENV = os.getenv('FLASK_ENV', 'development')


if(FLASK_ENV == 'production'):
    app.config.from_object(prod)
else:
    app.config.from_object(default)