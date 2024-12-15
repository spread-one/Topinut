import os
from app import create_app
from models import db

# 데이터베이스 초기화 코드 추가
def initialize_database():
    """schema.sql을 실행하여 초기 테이블 생성"""
    with open('db/schema.sql', 'r') as file:
        schema_sql = file.read()

    with db.engine.connect() as connection:
        connection.execute(schema_sql)

app = create_app()

if __name__ == '__main__':
    # 데이터베이스 초기화 (schema.sql 실행)
    initialize_database()
    
    # Flask 앱 실행
    app.run(debug=True)
