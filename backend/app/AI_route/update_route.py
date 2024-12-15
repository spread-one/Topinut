from flask import Blueprint, request, jsonify
from models import db, ErrorCategory  # models.py에서 import
import json

# Blueprint 생성
update_db_bp = Blueprint('update_db', __name__)

@update_db_bp.route('/api/update-db', methods=['POST'])
def update_db():
    """
    클라이언트로부터 받은 카테고리 데이터를 기반으로 DB를 업데이트합니다.
    """
    try:
        data = request.get_json()
        print(f"📢 받은 데이터: {data}")  # 데이터 확인

        if not data or 'categories' not in data:
            print(f"🚨 오류 발생 - 요청 데이터가 없습니다: {data}")
            return jsonify({"error": "categories 키가 요청 데이터에 존재하지 않습니다."}), 400

        categories = data.get('categories')

        # 🚨 categories가 문자열로 들어오는 경우 JSON 디코딩
        if isinstance(categories, str):
            try:
                categories = json.loads(categories)
            except json.JSONDecodeError as e:
                print(f"🚨 오류 발생 - JSON 디코딩 오류: {e}")
                return jsonify({"error": "categories 키의 값이 잘못된 JSON 문자열입니다."}), 400

        # 🚨 categories가 리스트가 아니면 오류 발생
        if not isinstance(categories, list):
            print(f"🚨 오류 발생 - categories 데이터가 list가 아닙니다. 받은 데이터: {categories}")
            return jsonify({"error": "유효한 categories 데이터가 필요합니다. (list 형태여야 함)"}), 400

        # 🚨 categories 내부의 항목들에 대해 유효성 검사
        for category in categories:
            if 'category_name' not in category or 'increment' not in category:
                print(f"🚨 오류 발생 - category_name 또는 increment 키가 누락되었습니다. 데이터: {category}")
                return jsonify({"error": "category_name 또는 increment 키가 누락되었습니다."}), 400

            if not isinstance(category['category_name'], str) or not isinstance(category['increment'], int):
                print(f"🚨 오류 발생 - category_name은 문자열, increment는 정수여야 합니다. 데이터: {category}")
                return jsonify({"error": "category_name은 문자열, increment는 정수여야 합니다."}), 400

        # 🚀 데이터가 정상이라면 빈도 업데이트 실행
        update_category_frequencies(categories)
        return jsonify({"message": "카테고리 빈도가 성공적으로 업데이트되었습니다."})

    except Exception as e:
        print(f"❌ 내부 서버 오류: {e}")
        return jsonify({"error": f"내부 서버 오류가 발생했습니다: {e}"}), 500


def update_category_frequencies(categories):
    """
    카테고리 빈도를 업데이트합니다.
    """
    try:
        for category in categories:
            category_name = category['category_name']
            increment = category['increment']

            # 기존 카테고리의 frequency를 업데이트
            category_record = ErrorCategory.query.filter_by(category_name=category_name).first()
            if category_record:
                category_record.frequency += increment
                db.session.add(category_record)

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(f"DB 업데이트 오류: {e}")
