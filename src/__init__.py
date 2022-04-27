import os
from flask import Flask 
# import src.routes.init_routes as init_routes
import routes.init_routes as init_routes

def charger_routes(app: Flask):
    app.register_blueprint(init_routes.init_app_routes)

# from sqlalchemy import create_engine
def init_app() -> Flask:
    app = Flask(__name__, template_folder='templates')
    charger_routes(app)
    return app
