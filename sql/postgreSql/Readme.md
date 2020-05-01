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