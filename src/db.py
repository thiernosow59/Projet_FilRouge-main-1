from flask import *
from pymongo import *

client = MongoClient('mongo', 27017, username='admin', password='root')
# client = MongoClient('localhost', port=27017)

db = client.bdd_projet
utilisateur = db.utilisateur

def save_user(email, password, nom, prenom):
    utilisateur.insert_one({email: email, password: password, nom: nom, prenom: prenom })

def get_users(): 
    return db.utilisateur.find({})