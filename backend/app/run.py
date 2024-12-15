import os
from flask import Flask, render_template, jsonify, request
from config import Config
from models import db, ErrorCategory
from AI_route.chatbot_route import chatbot_bp
from AI_route.question_generation_route import qg_bp
from AI_route.scroing_route import scoring_bp
from AI_route.write_profreading_route import writepro_bp
from AI_route.category_route import category_bp

# Flask 애플리케이션 인스턴스 생성
app = Flask(__name__, template_folder='templates')

# Config 설정 불러오기
app.config.from_object(Config)

# 블루프린트 등록
app.register_blueprint(chatbot_bp)
app.register_blueprint(qg_bp)
app.register_blueprint(scoring_bp)
app.register_blueprint(writepro_bp)
app.register_blueprint(category_bp)
# SQLAlchemy 초기화
db.init_app(app)

def insert_initial_data():
    initial_categories = [
        {"category_name": "맞춤법 오류", "frequency": 0},
        {"category_name": "문법 오류", "frequency": 0},
        {"category_name": "조사 오류", "frequency": 0},
        {"category_name": "높임말 오류", "frequency": 0},
        {"category_name": "어순 오류", "frequency": 0},
        {"category_name": "의미 중복 오류", "frequency": 0},
        {"category_name": "부사 사용 오류", "frequency": 0},
        {"category_name": "동사 활용 오류", "frequency": 0},
        {"category_name": "명사 사용 오류", "frequency": 0},
        {"category_name": "형용사 사용 오류", "frequency": 0},
        {"category_name": "문장 연결 오류", "frequency": 0},
        {"category_name": "구두점 오류", "frequency": 0},
        {"category_name": "텍스트 일관성 오류", "frequency": 0},
        {"category_name": "대명사 사용 오류", "frequency": 0},
        {"category_name": "고유명사 표기 오류", "frequency": 0},
        {"category_name": "불필요한 반복 오류", "frequency": 0},
        {"category_name": "접속사 사용 오류", "frequency": 0},
        {"category_name": "생략 오류", "frequency": 0},
        {"category_name": "문장 분리 오류", "frequency": 0},
        {"category_name": "문체 오류", "frequency": 0},
    ]

    # 중복 데이터 방지
    for category in initial_categories:
        existing = ErrorCategory.query.filter_by(category_name=category["category_name"]).first()
        if not existing:
            new_category = ErrorCategory(
                category_name=category["category_name"],
                frequency=category["frequency"]
            )
            db.session.add(new_category)
    db.session.commit()
    print("초기 데이터가 성공적으로 삽입되었습니다.")
# 기본 경로: templates 폴더의 index.html 렌더링
@app.route('/')
def home():
    """
    기본 경로로 접속하면 templates/index.html 파일을 렌더링합니다.
    """
    return render_template('index.html')

# /chatbot 경로: templates 폴더의 chatbot.html 렌더링
@app.route('/chatbot')
def chatbot():
    """
    /chatbot 경로로 접속하면 templates/chatbot.html 파일을 렌더링합니다.
    """
    return render_template('chatbot.html')
@app.route('/profread')
def prof():
    """
    """
    return render_template('profread.html')
@app.route('/generate')
def gen():
    return render_template('qgen.html')
# API 예제
@app.route('/api/example', methods=['GET'])
def example_api():
    """
    API 엔드포인트 예시
    """
    return jsonify({"message": "Hello from Flask API"})

if __name__ == '__main__':
    with app.app_context():
        # 데이터베이스 초기화
        db.create_all()
        insert_initial_data()
    app.run(debug=True, port=5000)
