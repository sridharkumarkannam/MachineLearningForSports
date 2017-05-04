Scripts for building the database.

# TennisDB Schema

To connect to the tennis database
```
psql postgres://[USERNAME]:[PASSWORD]@tennis.c5iuadtwr2db.us-east-1.rds.amazonaws.com:5432/tennisdb
```
ask @albscui for the username and password.


## Table: `player`
```sql
CREATE TABLE IF NOT EXISTS player (
            id integer PRIMARY KEY,
            firstName varchar(100),
            lastName varchar(100),
            hand char(1),
            birth char(8),
            country char(3)
);
```

In terminal, enter the following to copy data to the database
```bash
cat atp_players.csv | psql postgres://[USERNAME]:[PASSWORD]@tennis.c5iuadtwr2db.us-east-1.rds.amazonaws.com:5432/tennisdb -c "\copy player(id, firstName, lastName, hand, birth, country) from stdin DELIMITER ',' CSV"
```


