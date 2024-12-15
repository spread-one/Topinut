from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..config import Config
from ..models import db

def create_app():
    app = Flask(__name__)

    # Flask 설정 로드
    app.config.from_object(Config)

    # SQLAlchemy 초기화
    db.init_app(app)

    return app
