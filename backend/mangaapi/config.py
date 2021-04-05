"""
config.py
- settings for the flask application object
"""

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True    
    SECRET_KEY = 'p9Bv<3Eid9%$i01090fdcxzas'
    SQLALCHEMY_DATABASE_URI = 'mysql://kami:kami123@localhost/Manga_db'