import os
from flask import Flask

app = Flask(__name__)
def create_app():
    return app