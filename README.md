# SQLAlchemy Starter Pack
The purpose of this repository is to provide you with a simple boilerplate 
setup to practice the basics of interfacing with a database using SQLAlchemy. 
I have provided you a series of tasks found within the `/app/models/__init__.py` 
file and `/app/__init__.py` along with solutions in respective step files.

## Guided Exercise Goals
This workspace will focus primarily on interacting with a database 
using SQLAlchemy. If you would like to follow along, I have included instructions and practice tasks.
If you would rather use this to go off on your own learning adventure, it is equipped for that too.
Hopefully if you are able to get through these exercises you will feel 
comfortable with the following skills after.

1. Creating db structures
2. Modifying db structures
3. Creating, modifying, & Retrieving db data using a REST endpoint

Begin by opening the `/app/models/__init__.py` file and reading the instructions there. 
Once you have completed the model manipulation tasks, you can move onto the database 
interaction tasks in the app root dunder init located `/app/__init__.py`.

I've included a Postman collection export called SQLAlchemy_Playground.postman_collection.json. 
These postman calls corresponds with each of the sample solution REST endpoints. You can use 
these to compare or recreate your own endpoint tests.

## Local Setup
This is a pretty basic setup configured to leverage a local sqlite database. You can extend this to fit your needs 
by modifying the environment variables in the env.default file. 

1. Install dependencies 
``` 
cd sqlalchemy-playground
pip install -r requirements.txt
```

2. Set up local environment variables
```
cp .env.default .env
```

3. This setup leverages the [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) library for migrations. If you choose 
to use this for your work you will need to also run the following command in your terminal before you can create migration versions:
``` 
 flask db init
```
If you receive an error stating something like "No such command init-db", you may need to export your FLASK_APP environment variable explicitly.

## Making Database Changes with Flask-Migrate 

### Creating a migration version
DB structure changes with migrations are accomplished by running upgrades on a 
migration version. The following command will generate a new migration version file
for you. Be sure to include a clear description of what changes this version contains. 
It will be helpful in the future!
```
flask db migrate -m "Your descriptive message here"
```

### Ugrading and Downgrading
Migrations give you a handy simple way to implement and roll back database structure changes. 
In each of the migration version files you generate, you will find a method for upgrading, which 
will contain commands to implement all the changes you made on your database, and downgrading, 
which will be the inverse. The following commands can be run in your terminal to perform the changes.

#### Implement DB Changes
```
flask db upgrade
```

#### Roll-back DB Changes
```
flask db downgrade
```

## Resources
- [SqlAlchemy Models & Tables Documentation](https://flask-sqlalchemy.readthedocs.io/en/stable/models/)
- [Flask-Migrate Documentation](https://flask-migrate.readthedocs.io/en/latest/)
- [URL format for connecting a different type of DB](https://flask-sqlalchemy.readthedocs.io/en/stable/config/)
- Bonus exploration into data validation using [Pydantic](https://pypi.org/project/pydantic/) or [Marshmallow](https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html)

## Requirements
- Python 3.13 or higher
- SQLAlchemy 1.4.0 or higher