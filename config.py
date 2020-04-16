import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL - DONE
SQLALCHEMY_DATABASE_URI = "postgres://wisdomidi:Sososoweto2010@localhost:5432/fyyur"
#SQLALCHEMY_DATABASE_URI = "postgres://xqpumnqcsjjpaa:4a81ee23944c334175c4809089519af0a029f6448079f15d66d4be58d433df75@ec2-3-211-48-92.compute-1.amazonaws.com:5432/ddod2t9f2hp648"

SQLALCHEMY_TRACK_MODIFICATIONS = False
