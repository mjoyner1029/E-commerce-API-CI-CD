from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
db = SQLAlchemy(app)
swagger = Swagger(app)

from app import routes
