class Config:
    # Flask 기본 설정
    SECRET_KEY = "your_secret_key"
    DEBUG = True

    # MySQL 데이터베이스 설정 (환경 변수 사용 안 함)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/topik_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
