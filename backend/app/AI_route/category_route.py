from flask import Blueprint, request, jsonify
from AI_service.category_service import export_category

# Blueprint 생성
category_bp = Blueprint('category', __name__)

@category_bp.route('/api/category', methods=['POST'])
def get_category():
    
    """
    사용자의 첨삭 데이터를 받아 GPT-4를 통해 카테고리를 추출하는 API 엔드포인트.
    """
    try:
        data = request.get_json()
        user_input = data.get('user_input')

        if not user_input:
            return jsonify({"error": "user_input이 필요합니다."}), 400

        # GPT-4의 카테고리 추출 서비스 호출
        response = export_category(user_input)
        return jsonify({"categories": response})
    
    except Exception as e:
        return jsonify({"error": f"오류가 발생했습니다: {e}"}), 500