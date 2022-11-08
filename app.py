import os
from dotenv import load_dotenv
from . import create_app
from . import DBConnection
from . import route

load_dotenv()
app = create_app()
DBConnection.connect()
