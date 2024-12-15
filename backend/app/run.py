import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from app.config import Config
from app.models import db, Problem, ErrorCategory, ErrorDetail

# Flask 애플리케이션 초기화
app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
app.config.from_object(Config)

# CORS 설정
CORS(app)

# SQLAlchemy 초기화
db.init_app(app)

# 데이터베이스 초기화 및 초기 데이터 추가
def initialize_database():
    """
    데이터베이스 테이블 생성 및 초기 데이터 추가
    schema.sql 파일을 실행해 테이블을 만들고,
    초기 데이터가 없으면 기본 데이터 삽입
    """
    # schema.sql 파일 실행
    if os.path.exists("db/schema.sql"):
        with open("db/schema.sql", "r") as file:
            schema_sql = file.read()
        with db.engine.connect() as connection:
            connection.execute(schema_sql)
    
    # 초기 데이터 삽입
    with app.app_context():
        db.create_all()  # 테이블 생성
        if not ErrorCategory.query.first():  # 이미 데이터가 존재하는지 확인
            error_category1 = ErrorCategory(category_name='문법', frequency=0)
            error_category2 = ErrorCategory(category_name='어휘', frequency=0)
            db.session.add_all([error_category1, error_category2])
            db.session.commit()

# React 빌드 파일 서빙
@app.route('/')
def serve_react_app():
    """React 빌드 파일의 index.html 제공"""
    return send_from_directory(app.static_folder, "index.html")

# 정적 파일 제공 (CSS, JS 등)
@app.route('/<path:path>')
def serve_static_files(path):
    """React 빌드 폴더 내의 정적 파일 제공"""
    return send_from_directory(app.static_folder, path)

# API 엔드포인트 예시
@app.route('/api/example', methods=['GET'])
def example_api():
    """API 예제 라우트"""
    return {"message": "Hello from Flask API"}

# 메인 실행
if __name__ == '__main__':
    # 데이터베이스 초기화
    with app.app_context():
        initialize_database()

    # Flask 앱 실행
    app.run(debug=True)
