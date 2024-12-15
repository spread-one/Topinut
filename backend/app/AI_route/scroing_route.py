from flask import Blueprint, request, jsonify
from AI_service.scoring_service import get_scoring

# 블루프린트 생성
scoring_bp = Blueprint('scoring', __name__)

@scoring_bp.route('/api/scoring', methods=['POST'])
def scoring():
    """
    사용자의 문제와 답변을 받아 GPT-4의 점수를 반환하는 API 엔드포인트.
    
    Request:
        - JSON 데이터: {"problem": "<문제>", "answer": "<답변>"}
    
    Response:
        - JSON 데이터: {"response": "<GPT의 평가 결과>"}
    """
    try:
        # 요청에서 JSON 데이터 가져오기
        data = request.get_json()
        problem = data.get('problem')  # 문제 입력
        answer = data.get('answer')    # 답변 입력

        # 입력값 검증
        if not problem or not answer:
            return jsonify({"error": "problem과 answer가 필요합니다."}), 400

        # 서비스 로직 호출
        response = get_scoring(problem, answer)
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": f"오류가 발생했습니다: {e}"}), 500
