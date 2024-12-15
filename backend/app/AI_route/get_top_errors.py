from flask import Blueprint, jsonify
from models import db, ErrorCategory

error_bp = Blueprint('error', __name__)

@error_bp.route('/api/get-top-errors', methods=['GET'])
def get_top_errors():
    """
    데이터베이스에서 frequency가 높은 상위 5개의 error_category를 가져옵니다.
    """
    try:
        errors = ErrorCategory.query.order_by(ErrorCategory.frequency.desc()).limit(5).all()
        result = [
            {"category_name": error.category_name, "frequency": error.frequency} 
            for error in errors
        ]
        return jsonify({"errors": result})
    except Exception as e:
        return jsonify({"error": f"서버 오류: {e}"}), 500
