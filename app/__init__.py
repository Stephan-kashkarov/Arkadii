from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import configure_app

app = Flask(__name__)
configure_app(app, config)
db = SQLAlchemy()
migrate = Migrate(db)
cors = CORS(app, resources={
    r'/api/*': {
        'origins': app.config['ORIGINS']
    }
})
