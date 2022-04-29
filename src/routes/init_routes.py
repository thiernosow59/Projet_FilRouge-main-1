from flask import Flask, render_template, request, redirect, url_for, Blueprint  
from src.db import *
# from db import *

init_app_routes = Blueprint('init_routes', __name__)

#   page d'accueil du site permettant de ce connecter
@init_app_routes.route("/")
@init_app_routes.route("/accueil")
def accueil():
    # users = get_users()
    # for user in users: 
    #   print(user)
      # return "Bonjour"
    return render_template('accueil.html')


@init_app_routes.route("/index", methods=['GET', 'POST'])
def index():
      if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        save_user(username, password)
        return redirect(url_for('init_routes.accueil'), msg=msg)
      return render_template('index.html')

#   page d'inscription du site
@init_app_routes.route("/inscription", methods=['GET', 'POST'])
def inscription():
      if request.method == 'POST':
         prenom = request.form.get('prenom')
         nom = request.form.get('nom')
         email = request.form.get('email')
         password = request.form.get('password')
      #    confpassword = request.get.form('password')
      #    if(confpassword == password):
         save_user(email,password,nom,prenom)   
         return redirect(url_for('init_routes.accueil'))
      return render_template('inscription.html')
