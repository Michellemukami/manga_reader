"""
models.py
- Data classes for the manga application
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Manga_details(db.Model):
    __tablename__ = 'manga_details'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    genre = db.Column(db.Text)
    author = db.Column(db.Text)
    rating = db.Column(db.Text)
    chapters = db.relationship('manga_chapters', backref='chapter', lazy=True)
    summary = db.Column(db.Text)
   

class Manga_chapters(db.Model):
    __tablename__ = 'manga_chapters'

    id = db.Column(db.Integer, primary_key=True)
    images = db.Column(db.String(264), unique=True)
    manga_id = db.Column(db.Integer, db.ForeignKey('manga_details.id'),nullable=False)

    
  