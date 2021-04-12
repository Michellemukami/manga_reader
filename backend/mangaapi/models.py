"""
models.py
- Data classes for the manga application
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Manga_details(db.Model):
    __tablename__ = 'manga_details'

    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100))  
    author = db.Column(db.String(100))
    summary = db.Column(db.Text)

class Manga_images(db.Model):
    __tablename__ = 'manga_images'

    id = db.Column(db.Integer, primary_key=True)   
    file_path = db.Column(db.String(100))
    file_type = db.Column(db.String(100))
    mime_type = db.Column(db.String(100))
    
   
class Manga_chapter(db.Model):
    __tablename__ = 'manga_chapter'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    issue_no = db.Column(db.Integer)
    
class Manga_chap_image(db.Model):
    __tablename__ = 'manga_chap_image'

    id = db.Column(db.Integer, primary_key=True)
    manga_image_id = db.Column(db.Integer, db.ForeignKey('manga_images.id'),nullable=False) 
    manga_chap_id = db.Column(db.Integer, db.ForeignKey('manga_chapter.id'),nullable=False) 

class Manga_genre(db.Model):
    __tablename__ = 'manga_genre'

    id = db.Column(db.Integer, primary_key=True)
    genre_title = db.Column(db.String(100), unique=True)
    
class Manga_chap_genre(db.Model):
    __tablename__ = 'manga_chap_genre'

    id = db.Column(db.Integer, primary_key=True)
    manga_genre_id = db.Column(db.Integer, db.ForeignKey('manga_genre.id'),nullable=False)
    manga_details_id = db.Column(db.Integer, db.ForeignKey('manga_details.id'),nullable=False) 
    


    

    

    
  