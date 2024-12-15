from flask import Blueprint, request, jsonify
from AI_service.question_generation_service import get_question_generation

# Blueprint 초기화
qg_bp = Blueprint('qg', __name__)

@qg_bp.route('/api/qgen', methods=['POST'])
def questiongen():
    """
    TOPIK 시험 문제를 생성하는 API 엔드포인트
    
    Request:
        - 요청에 입력은 필요하지 않음.
    
    Response:
        - JSON 데이터: {"response": "<GPT의 응답>"}
    """
    try:
        # 서비스 로직 호출 (question_generation_service.py)
        response = get_question_generation()
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": f"오류가 발생했습니다: {e}"}), 500
