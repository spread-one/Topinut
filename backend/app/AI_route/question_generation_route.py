from flask import Flask, request, jsonify
from app.AI_service.question_generation_service import get_question_generation

app = Flask(__name__)

@app.route('/api/qgen', methods=['POST'])
def chatbot():
    """
    사용자의 입력을 받아 GPT-4의 응답을 반환하는 API 엔드포인트.
    
    Request:
        - JSON 데이터: {"user_input": "<사용자 입력>"}
    
    Response:
        - JSON 데이터: {"response": "<GPT의 응답>"}
    """
    try:
        # 요청에서 JSON 데이터 가져오기
        data = request.get_json()
        user_input = data.get('user_input')

        if not user_input:
            return jsonify({"error": "user_input이 필요합니다."}), 400

        # 서비스 로직 호출 (chatbot_service.py)
        response = get_question_generation(user_input)
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": f"오류가 발생했습니다: {e}"}), 500
