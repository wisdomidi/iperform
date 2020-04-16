import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL - DONE
SQLALCHEMY_DATABASE_URI = "postgres://wisdomidi:Sososoweto2010@localhost:5432/fyyur"
#SQLALCHEMY_DATABASE_URI = 'postgres://alanabellucci@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
