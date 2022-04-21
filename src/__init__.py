import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, session  
from .db import save_malade as save_malade

# from sqlalchemy import create_engine
def init_app() -> Flask:
    app = Flask(__name__)
    
#   page d'accueil du site permettant de ce connecter
    @app.route("/accueil", methods =['GET'])
    def accueil():
        return render_template('accueil.html')
    
    @app.route("/index", methods =['GET', 'POST'])
    def index():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            save_malade(username,password)    
            return redirect(url_for('accueil'))
        return render_template('index.html')

#   page d'inscription du site
    @app.route("/inscription", methods =['GET', 'POST'])
    def inscription():
        if request.method == 'POST':
            username = request.get.form('username')
            return redirect(url_for('accueil'))
        return render_template('inscription.html')
    
    return app
