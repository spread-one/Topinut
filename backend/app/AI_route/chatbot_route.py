from flask import Blueprint, request, jsonify
from AI_service.chatbot_service import get_chatbot_response

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/api/chatbot', methods=['POST'])
def chatbot():
    """
    사용자의 입력을 받아 GPT-4의 응답을 반환하는 API 엔드포인트.
    """
    try:
        data = request.get_json()
        user_input = data.get('user_input')

        if not user_input:
            return jsonify({"error": "user_input이 필요합니다."}), 400

        # GPT-4의 응답 가져오기
        response = get_chatbot_response(user_input)
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": f"오류가 발생했습니다: {e}"}), 500
