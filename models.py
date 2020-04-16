#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask_sqlalchemy import SQLAlchemy

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models. iperform
#----------------------------------------------------------------------------#

class Venue(db.Model):
  __tablename__ = 'venues'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  address = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  genres = db.Column(db.ARRAY(db.String(120)))
  website = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, nullable = False, default = False)
  seeking_description = db.Column(db.String(500))
  # TODO: implement any missing fields, as a database migration using Flask-Migrate - DONE

  artists = db.relationship('Artist', secondary = 'shows') #relates Venue to Show via Artist, this is a bidirectional relationship

  # return a dictionary of venues
  def venue_to_dictionary(self):
    return{
        'id' : self.id,
        'name' : self.name,
        'city' : self.city,
        'state' : self.state,
        'address' : self.address,
        'phone' : self.phone,
        'image_link' : self.image_link,
        'facebook_link' : self.facebook_link,
        'genres' : self.genres,
        'website' : self.website,
        'seeking_talent' : self.seeking_talent,
        'seeking_description' : self.seeking_description
    }

  def __repr__(self):
    return f'<Venue Id: {self.id}, Name: {self.name}>'

class Artist(db.Model):
  __tablename__ = 'artists'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.ARRAY(db.String(120)))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  website = db.Column(db.String(120))
  seeking_venue = db.Column(db.Boolean, nullable = False, default = False)
  seeking_description = db.Column(db.String(500))
  # TODO: implement any missing fields, as a database migration using Flask-Migrate - DONE

  venues = db.relationship('Venue', secondary='shows') #relates Artist to Show via Venue, this is a bidirectional relationship

  # return a dictionary of artists
  def artist_to_dictionary(self):
    return{
        'id' : self.id,
        'name' : self.name,
        'city' : self.city,
        'state' : self.state,
        'phone' : self.phone,
        'genres' : self.genres,
        'image_link' : self.image_link,
        'facebook_link' : self.facebook_link,
        'website' : self.website,
        'seeking_venue' : self.seeking_venue,
        'seeking_description' : self.seeking_description
    }


  def __repr__(self):
    return f'<Artist Id: {self.id}, Name: {self.name}>'

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration. - DONE
class Show(db.Model):
  __tablename__ = 'shows'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), primary_key = True) #venues is the table name, not the name of the class
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), primary_key = True) #artists is the table name, not the name of the class
  start_time = db.Column(db.DateTime, nullable = False)

  venue = db.relationship('Venue') # allows us to call Venue fields on Show
  artist = db.relationship('Artist') # allows us to call Artist fields on Show

  #returns a dictionary of artists for the show
  def show_artist(self):
    return {
        'artist_id' : self.artist_id,
        'artist_name' : self.artist.name,
        'artist_image_link' : self.artist.image_link,
        'start_time' : self.start_time
    }

  #returns a dictionary of venues for the show
  def show_venue(self):
    return {
        'venue_id' : self.venue_id,
        'venue_name' : self.venue.name,
        'venue_image_link' : self.venue.image_link,
        'start_time' : self.start_time
    }






