import os;

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# create engine is used to access the data from the system
engine = create_engine(os.getenv("DATABASE_URL"))
# scoped_session create different session for every user  
db = scoped_session(sessionmaker(bind=engine))  