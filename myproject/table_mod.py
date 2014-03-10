# table_mod.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic2.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# querying for a record in the Artist table
#res = session.query(Artist).filter(Artist.name=="Kutless").first()
#print res.name
 
# changing the name
#res.name = "Beach Boys"
#session.commit()
 
# editing Album data
artist, album = session.query(Artist, Album).filter(Artist.id==Album.artist_id).filter(Album.title=="Parade of the Athletes").first()
album.genre = "Trance"
session.commit()