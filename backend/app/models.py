from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 인스턴스 생성
db = SQLAlchemy()

class Problem(db.Model):
    __tablename__ = 'problems'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class ErrorCategory(db.Model):
    __tablename__ = 'error_categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False, unique=True)
    frequency = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class ErrorDetail(db.Model):
    __tablename__ = 'error_details'
    id = db.Column(db.Integer, primary_key=True)
    error_category_id = db.Column(db.Integer, db.ForeignKey('error_categories.id'), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('problems.id'), nullable=False)

    # 관계 설정
    error_category = db.relationship('ErrorCategory', backref='error_details')
    problem = db.relationship('Problem', backref='error_details')
