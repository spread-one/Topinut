from flask import Blueprint, request, jsonify
from AI_service.write_profreading_service import write_profreading

writepro_bp = Blueprint('writepro', __name__, url_prefix='/api')

@writepro_bp.route('/profread', methods=['POST'])
def profreading():
    """
    사용자의 문제와 답변을 받아 GPT-4의 첨삭 응답을 반환하는 API 엔드포인트.
    """
    try:
        data = request.get_json()
        problem = data.get('problem')  # 문제 입력
        answer = data.get('answer')   # 답변 입력

        if not problem or not answer:
            return jsonify({"error": "problem과 answer가 필요합니다."}), 400

        # GPT-4의 응답 가져오기
        response = write_profreading(problem, answer)
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": f"오류가 발생했습니다: {e}"}), 500
