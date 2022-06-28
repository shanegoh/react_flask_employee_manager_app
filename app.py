from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'iCuytwshTX'
app.config['CORS_HEADERS'] = 'Content-Type'


if __name__ == "__main__":
    app.run(debug=True)

# import declared routes
import routes
# Set up db connection
import db