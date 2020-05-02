# PostgreSql
- Setup Environment in Psql "https://www.tutorialspoint.com/postgresql/postgresql_environment.htm"
```javascript
   // Command of psql
   1. sudo systemctl start postgresql    // to starting the postgresql 
   2. sudo -u postgres createuser --interactive // creating user
   3. sudo postgres  // change root to postgresql  bash 
   4. psql -l        // return of list of existing table in database
   5. createdb <databaseName>    // command to create database in postgresql
   6. psql <databaseName>   // to enter your database
   7. service postgresql restart // for restarting server of psql
   8. \d     // to check the table but It should be after getting enter the database
   9. CREATE USER <username> WITH PASSWORD <password> 
   // creating user with password which help to access data base by creating server
   10. GRANT ALL PRIVILEGES ON TABLE <tableName> To <username>     // to get the access of of table for particular username and add this username for creating aql server
   11. grant all on sequence <fligts_id_seq> to <username> // to give the grant to use the table by username