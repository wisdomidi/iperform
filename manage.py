from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import db, Artist, Venue, Show

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
#test

if __name__ == '__main__':
    manager.run()
