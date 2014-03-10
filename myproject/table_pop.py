# table_pop.py

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic2.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Tiesto")
new_artist.albums = [Album("Escape Me", 
                           "Trance",
                           "NA", "CD")]
 
# add more albums
more_albums = [Album("Hell Is for Wimps",
                     "rock",
                     "Star Song", "CD"),
               Album("Love Liberty Disco", 
                     "testing",
                     "Sparrow", "CD"),
               Album("Thrive",
                     "testing",
                     "Sparrow", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("Tiesto"),
    Artist("Kaskade"),
    Artist("Benny Benassi")
    ])
session.commit()