from flask import Flask
from app.config import Config
from app.models import db, Problem, ErrorCategory, ErrorDetail

def create_app():
    app = Flask(__name__)

    # 설정 추가
    app.config.from_object(Config)

    # SQLAlchemy 초기화
    db.init_app(app)

    # 데이터베이스 초기화 및 초기 데이터 추가
    with app.app_context():
        db.create_all()

        if not ErrorCategory.query.first():  # 이미 데이터가 존재하는지 확인
            error_category1 = ErrorCategory(category_name='문법', frequency=0)
            error_category2 = ErrorCategory(category_name='어휘', frequency=0)
            db.session.add_all([error_category1, error_category2])

        db.session.commit()  # 데이터베이스에 변경 사항 적용
    
    return app
