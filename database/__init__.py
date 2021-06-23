
from flask_sqlalchemy import SQLAlchemy 
from app import app

DB = SQLAlchemy(app)

from database import models