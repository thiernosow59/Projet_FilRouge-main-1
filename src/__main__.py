import os  # module contenant des fonctions liées aux info sur l'OS
from flask import Flask, jsonify, render_template, Blueprint
from . import init_app
# from __init__ import init_app

# Création de l'application
# template_folder : emplacement des fichiers html
app = init_app()

# exemple d'utilisation des variables d'environnement
PORT = int(os.environ.get('SRV_PORT', 9000))
DEBUG = os.environ.get('SRV_DEBUG', True)
HOST = os.environ.get('SRV_HOST', '0.0.0.0')
# app.config["MONGO_URL"] = 'mongodb://admin:root@localhost:27017/'
app.config["MONGO_URL"] = "mongodb+srv://admin:root@mongo:27017?ssl=true&ssl_cert_reqs=CERT_NONE"

# DB_STRING = os.environ.get(
#     'DB_STRING', 'mysql+pymysql://root:root@localhost:3310/app')
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_STRING
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)

# démarrage du serveur
if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
