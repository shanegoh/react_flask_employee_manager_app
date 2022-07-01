from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'iCuytwshTX'
app.config['CORS_HEADERS'] = 'Content-Type'


if __name__ == "__main__":
    app.run(debug=True)

# import declared routes
import routes
# import declared auth
import auth
# Set up db connection
import db