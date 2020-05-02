import os;
from sqlalchemy import create_engine;
from sqlalchemy.orm import scoped_session,sessionmaker;

engine = create_engine('postgresql://prabhatku:1234@localhost/airport');
db = scoped_session(sessionmaker(bind=engine))

def main():

    f_id = int(input("Enter flight id - "));

    flight = db.execute("SELECT origin,destination,duration FROM fligts WHERE id = :id",
                             {"id":f_id}).fetchone();
    if flight is None:
        print("Fight does not exist");
        return;
    
    passenger = db.execute("SELECT name FROM passangers WHERE flight_id = :id",
                      {"id":f_id}).fetchall()
    
    print("\nPassengers List : ");
    if len(passenger) == 0:
        print("No passanger exist in this Flight try Some other flight id");
        return
    for pas in passenger:
        print(pas.name)
    

if __name__ == '__main__':
    main()
    