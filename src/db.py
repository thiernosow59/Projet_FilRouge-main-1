from flask import *
from pymongo import *

client = MongoClient('localhost', port=27017, username='admin', password='root')

db = client.bdd_projet


def save_malade(username, password):
    db.malade.insert_one({username: 'username ', password: 'password'})
