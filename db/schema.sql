-- 문제 테이블: 문제 정보와 기록된 점수를 저장
CREATE TABLE problems (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- 문제 ID
    content TEXT NOT NULL,               -- 문제 내용
    score INT CHECK (score BETWEEN 0 AND 100),  -- 기록된 점수 (0 ~ 100)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 생성 시간
);

-- 틀린 분야 테이블: 틀린 분야와 횟수를 저장
CREATE TABLE error_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- 틀린 분야 ID
    category_name VARCHAR(255) NOT NULL UNIQUE,  -- 틀린 분야 이름 (예: '문법', '어휘')
    frequency INT DEFAULT 0,             -- 틀린 횟수
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- 마지막 갱신 시간
);

-- 틀린 내용 테이블: 특정 문제와 틀린 분야를 연결
CREATE TABLE error_details (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- 틀린 내용 ID
    error_category_id INT NOT NULL,      -- 틀린 분야 ID (foreign key)
    problem_id INT NOT NULL,             -- 문제 ID (foreign key)
    FOREIGN KEY (error_category_id) REFERENCES error_categories(id) ON DELETE CASCADE,
    FOREIGN KEY (problem_id) REFERENCES problems(id) ON DELETE CASCADE
);
