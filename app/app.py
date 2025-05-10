from flask import Flask

from app.controller.getfile import getfile
from app.models.User import Base
from app.models.App import App

def create_app():
  app = App(Flask(__name__),
            SQLALCHEMY_DATABASE_URI = "postgresql://postgres:senha@db:5432/compsci",
            SQLALCHEMY_TRACK_MODIFICATIONS = False)
  app.add_routes("/getfile", "getfile", getfile, ['GET'])

  db = App.get_db()
  with app.get_app().app_context():
    if db is not None:
      Base.metadata.create_all(db.engine)

  return app.get_app()