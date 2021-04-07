"""
config.py
- settings for the flask application object
"""

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True    
    SECRET_KEY = 'p9Bvdsdraqwzrrzbrr<3bEid9%$i01090fdcxzas'
    SQLALCHEMY_DATABASE_URI = 'mysql://kami:kami123@localhost/Manga_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True