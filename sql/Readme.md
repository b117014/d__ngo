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

SELECT * from <tableName> WHERE <colmnName> LIKE '%a%'   // here % means any character and this syntax means that find the data where the columnName contains "a" character


```

``` javascript
   Ex- INSERT INTO flight
            (source, destination, date)
            INFO("Delhi","Bhubaneswar","6 May")