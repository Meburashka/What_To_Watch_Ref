# type: ignore
from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

from dotenv import load_dotenv
load_dotenv()  # Загружает .env

app = Flask(__name__)

# Указываем полный путь к settings.py относительно этого файла
# (__init__.py в opinions_app)
# ../settings.py означает "на уровень выше из opinions_app"
BASE_DIR = Path(__file__).resolve().parent.parent
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import Opinion
from . import views, models, forms, error_handlers, cli_commands
