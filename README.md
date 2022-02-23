
# RUN PROGRAM, add dependencies through pyproject.toml

- PYTHONPATH=./main poetry run python main/app.py // runs the app file 
- export FLASK_DEV=development // runs in debug mode


------------------------------------------------------

# Db connection command-line stats

PYTHONPATH=./main poetry run python main/create_table.py // run the create_table script to create tables

- fire up another terminal and type sqlite3 
- ./open database.db // opens a new database file
- ./tables ->display created tables
- select * from * user;  //display registered users
- drop table user; // test: change on the user models will not be displayed if running tables are not dropped and re-runned


---
23 February
- register user and add them to the database
- login schema and check_password to verify login
- 
