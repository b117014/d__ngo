# Sql

### Constraint Of Sql
- Primary Key
- Not Null
- Unique
- Check
- Default

## Syntax of Sql
```javascript
INSERT INTO <tablename> (<nameofcolumns>)           // insert row in table 
        INFO(<dataofeachcoulmn>);

SELECT * from <tableName> WHERE <colmnName> in ("") ;    // That's for to find the data ehere <colmnName> consist in ()

SELECT * from <tableName> WHERE <colmnName> LIKE '%a%'   // here % means any character and this syntax means that find the data where the columnName contains "a" character and "%a%" means that any character then a follow of any charcter.

UPDATE <tableName> 
      SET <colmnName> = ""        // updating the colomn data 

DELETE from <tableName>
        WHERE <colmnName> = ""   

SELECT * FROM <tableName> 
        ORDER BY <colmnName> ASC    //     arrange the data ascending order by <colmnnAME>

SELECT <col1>,<col2>,.. FROM <table1> JOIN <table2>  
         ON <table1.id> = <table2.id> WHERE <condn>;   // get data of two table ehere one table              referencing to others

CREATE TABLE <tablename>(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES <tablename2>
);
)

```

``` javascript
   Ex- INSERT INTO flight
            (source, destination, date)
            INFO("Delhi","Bhubaneswar","6 May")
   Ex- UPDATE flights
           SET duration = 30
           where origin = "New Delhi" ;
   Ex- DELETE from flights
             WHERE origin = "New Delhi" ;
   Ex- SECECT origin, COUNT(*) from flights 
             GROUP BY origin HAVING COUNT(*)>1;

```

## Agregation Function In SQl
1. AVG
2. MIN
3. MAX
4. COUNT
5. SUM

## Foregin Keys
- the key which helps to relate the multiple table .
- Foregin key is the referencing of the other table

## Types Of Join
1. JOIN / INNER JOIN
2. LEFT OUTER JOIN
3. RIGHT OUTER JOIN
4. FULL OUTER JOIN

- To resolve the Problem of Race Condition , Sql Transaction is used in database.

## Sql Transaction
1. BEGIN
2. COMMIT


## Sql and flask_alchemy

``` javascript

SELECT * FROM flights WHERE origin = "Paris" ;
------------------------------------------------
Flights.query.filter_by(origin="Paris").all() ;


SELECT * FROM flights WHERE id = 28;
------------------------------------------------
Flights.query.filter_by(id=28).first()   ||  Flights.query.get(28)


UPDATE flights SET duration =7 WHERE id = 3;
------------------------------------------------
flight = Flights.query.get(3)
flight.duration = 7


DELETE FROM flights where id=5;
------------------------------------------------
flight = Flights.query.get(5)
db.session.delete(flight)


COMMIT;
-----------------------------------------------
db.session.commit();


SELECT * FROM flights ORDER BY origin;
-----------------------------------------------
Flight.query.order_by(Flight.origin).all()


SELECT * FROM flights ORDER BY origin DESC;
-----------------------------------------------
Flight.query.order_by(Flight.origin.desc()).all()


SELECT * FROM flights WHERE origin != "Paris";
-----------------------------------------------
Flight.query.filter(Flight.origin != "Paris").all()


SELECT * FROM flights WHERE origin LIKE "%a%";
-----------------------------------------------
Flight.query.filter(Flight.origin.like("%a%")).all()


SELECT * FROM flights WHERE origin IN ('Tokyo','Paris');
---------------------------------------------------------
Flight.query.filter(Flight.origin.in_(['Tokyo','Paris'])).all()


SELECT * FROM flights WHERE origin = "Paris" AND duration > 5 ;
-----------------------------------------------------------------
Flight.query.filter(and_(Flight.origin == "Paris", Flight.duration > 5)).all()


SELECT * FROM flights JOIN passangers ON flights.id = passangers.flight_id;
---------------------------------------------------------------------------
db.session.query(Flight, Passanger).filter(Flight.id == Passanger.flight_id).all()


```

## HTTP Methods

- GET: retrieve resource
- POST: create new resource
- PUT: replace a resource
- PATCH: update a resource
- DELETE: delete a resource
