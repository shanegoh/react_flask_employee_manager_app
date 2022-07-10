from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'iCuytwshTX'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test_production'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import routes
import auth
import database
import models