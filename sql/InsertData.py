import os;
import csv
from sqlalchemy import create_engine;
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine('postgresql://prabhatku:1234@localhost/airport')
db = scoped_session(sessionmaker(bind=engine))

def main():
    file = open("./data/flights.csv")
    reader = csv.reader(file)
  
    for origin,destination,duration in reader:
        db.execute("INSERT INTO fligts (origin,destination,duration) VALUES (:origin,:destination,:duration)",
                      {"origin":origin,"destination":destination,"duration":duration})
    db.commit()   # save my changes
        

if __name__ == '__main__':
    main()