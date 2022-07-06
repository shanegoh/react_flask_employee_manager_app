from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)


app.config['SECRET_KEY'] = 'iCuytwshTX'
app.config['CORS_HEADERS'] = 'Content-Type'

# import all routes
import routes
# import declared auth
import auth
# Set up db connection
import db

# app.register_blueprint(api_manager_bp, url_prefix='/api/manager')
# app.register_blueprint(api_public_bp, url_prefix='/api')
