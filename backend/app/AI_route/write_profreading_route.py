import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from app.config import Config
from app.models import db, ErrorCategory

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
    schema.sql 파일을 실행해 테이블을 만들고, 초기 데이터가 없으면 기본 데이터 삽입
    """
    if os.path.exists("db/schema.sql"):
        with open("db/schema.sql", "r") as file:
            schema_sql = file.read()
        with db.engine.connect() as connection:
            connection.execute(schema_sql)

    with app.app_context():
        db.create_all()
        if not ErrorCategory.query.first():  # 초기 데이터가 없을 경우 추가
            error_category1 = ErrorCategory(category_name='문법', frequency=0)
            error_category2 = ErrorCategory(category_name='어휘', frequency=0)
            db.session.add_all([error_category1, error_category2])
            db.session.commit()

# API 엔드포인트
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    """
    사용자의 입력을 받아 GPT-4의 응답을 반환하는 API 엔드포인트.
    """
    data = request.get_json()
    user_input = data.get('user_input')
    # GPT-4 응답 예시
    gpt_response = f"GPT-4 Response for input: {user_input}"
    return jsonify({"response": gpt_response})

@app.route('/api/qgen', methods=['POST'])
def qgen():
    """
    사용자의 입력을 받아 GPT-4의 질문 생성 API.
    """
    data = request.get_json()
    user_input = data.get('user_input')
    # GPT-4 질문 생성 예시
    gpt_response = f"Generated question based on input: {user_input}"
    return jsonify({"response": gpt_response})

@app.route('/api/scoring', methods=['POST'])
def scoring():
    """
    사용자의 입력을 받아 GPT-4를 사용한 점수 평가 API.
    """
    data = request.get_json()
    user_input = data.get('user_input')
    # GPT-4 점수 평가 예시
    gpt_response = f"Scoring result for input: {user_input}"
    return jsonify({"response": gpt_response})

@app.route('/api/write_profreading', methods=['POST'])
def write_proofreading():
    """
    OpenAI GPT-4를 사용한 TOPIK 문제 첨삭 API.
    """
    data = request.get_json()
    problem = data.get('problem')
    answer = data.get('answer')
    # GPT-4 첨삭 예시
    gpt_response = f"Proofreading result for problem: {problem} with answer: {answer}"
    return jsonify({"result": gpt_response})

# React 빌드 파일 서빙
@app.route('/')
def serve_react_app():
    """React 빌드 파일의 index.html 제공"""
    return send_from_directory(app.static_folder, "index.html")

@app.route('/<path:path>')
def serve_static_files(path):
    """React 빌드 폴더 내의 정적 파일 제공"""
    return send_from_directory(app.static_folder, path)

# 메인 실행
if __name__ == '__main__':
    with app.app_context():
        initialize_database()
    app.run(debug=True)
