# todo-project-startupfon

Startupfon assignment, user authentication using Flask 


# Some command-line information to run the program:

- export FLASK_ENV=app.py // sets the run environment
- export FLASK_DEV=development // runs in debug mode
- poetry run flask run // we installed flask on poetry so run poetry first

------------------------------------------------------

# Db connection command-line stats

PYTHONPATH=./main poetry run python main/create_table.py // run the create_table script to create tables

- fire up another terminal and type sqlite3 
- ./open database.db // opens a new database file
- ./tables ->display created tables
- select * from * user;  //display registered users
- drop table user; // test: change on the user models will not be displayed if running tables are not dropped and re-runned
