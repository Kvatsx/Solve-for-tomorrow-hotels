import os

# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'