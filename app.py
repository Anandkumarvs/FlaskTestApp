import os
from dotenv import load_dotenv
from . import create_app
from . import DBConnection
from . import route
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
load_dotenv()
app = create_app()
DBConnection.connect()
from .route import *
