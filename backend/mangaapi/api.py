from flask import Blueprint, jsonify, request, current_app, url_for, Flask
from .models import db, Manga_details

api = Blueprint('api', __name__)

def fetch_transaction():
   
    transaction = Manga_details.query.all()
    print(transaction)