from flask_restful import Resource, Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/empolyees_db'
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)





from Api import models, routes