from typing import Dict, Callable, List
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class App:
  __instance: 'App' = None # Singleton instance of App
  __app: Flask
  __db: SQLAlchemy|None = None # Singleton instance of SQLAlchemy


  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super(App, cls).__new__(cls)
    return cls.__instance


  def __init__(self, app: Flask = None, **configs) -> None:

    if not hasattr(self, '_initialized'):  # Prevent reinitialization

      if app is None:
        raise ValueError("A Flask app instance must be provided.")

      self.__app = app
      self.configs(**configs)

      if App.__db is None:
        App.__db = SQLAlchemy(self.__app)

      self._initialized = True


  def configs(self, **configs: Dict) -> None:
    """
    Set the configurations for the Flask app.
    :param configs: A dictionary of configurations. Ex.: {'DEBUG': True, 'TESTING': True}.
    """
    for key, value in configs.items():
      self.__app.config[key] = value


  def add_routes(self, endpoint: str, endpoint_name: str, handler: Callable, methods: List[str], *args, **kwargs) -> None:
    """
    Add a route to the Flask app.

    :param endpoint: The endpoint for the route. Ex.: '/api'.
    :param endpoint_name: The name of the endpoint. Ex.: 'api'.
    :param handler: The handler function for the route.
    :param methods: The HTTP methods for the route. Ex.: ['GET', 'POST'].
    :param args: Additional arguments for the handler.
    :param kwargs: Additional keyword arguments for the handler.
    """
    self.__app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)


  def run(self, *args, **kwargs) -> None:
    """
    Run the Flask app.

    :param args: Additional arguments for the run method.
    :param kwargs: Additional keyword arguments for the run method.
    """
    self.__app.run(*args, **kwargs)

  @staticmethod
  def get_db() -> object|None:
    """
    Get the singleton instance of SQLAlchemy if exists.

    :return: The singleton instance of SQLAlchemy.
    """
    return App.__db


  @staticmethod
  def get_app() -> Flask|None:
    """
    Get the singleton instance of Flask if exists.

    :return: The singleton instance of Flask.
    """
    if App.__instance is None or App.__instance.__app is None:
      raise RuntimeError("The Flask app instance has not been initialized.")
    return App.__instance.__app