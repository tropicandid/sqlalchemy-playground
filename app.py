from config import Config
from extensions import db
from flask import Flask
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase
from routes import RestRoutes

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
import models
migrate = Migrate(app, db)
routes = RestRoutes(app, db)

if __name__ == "__main__":
    app.run(debug=True)