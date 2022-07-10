from flask import Flask

def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    from flask_cors import CORS
    from database import db
    CORS(app)
    app.config['SECRET_KEY'] = 'iCuytwshTX'
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test_production'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from routes.routes import routes_bp
        from routes.manager_routes import manager_routes_bp
        from routes.staff_routes import staff_routes_bp
        # Register Blueprints
        app.register_blueprint(manager_routes_bp, url_prefix='/api/manager')
        app.register_blueprint(routes_bp, url_prefix='/api')
        return app

