import os
from flask import Flask
from dotenv import load_dotenv


def configure_app():
    """configures the app and sets the env variables."""
    app = Flask(__name__)
    PROJECT_ROOT = os.path.dirname(__file__)
    load_dotenv(os.path.join(PROJECT_ROOT, '.environment_vars'))
    return app

