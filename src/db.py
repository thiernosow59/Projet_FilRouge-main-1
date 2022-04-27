from flask import *
from pymongo import *

# client = MongoClient('127.0.0.1', port=27017, username='admin', password='root')
client = MongoClient('127.0.0.1', port=27017)

db = client.bdd_projet

def save_user(email, password, nom, prenom):
    db.utilisateur.insert_one({email: 'email', password: 'password', nom: 'nom', prenom: 'prenom' })

def get_users(): 
    return db.utilisateur.find({})