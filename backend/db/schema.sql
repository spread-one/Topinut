-- 문제 테이블
CREATE TABLE IF NOT EXISTS problems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    score INT CHECK (score BETWEEN 0 AND 100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 틀린 분야 테이블
CREATE TABLE IF NOT EXISTS error_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE,
    frequency INT DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 틀린 내용 테이블
CREATE TABLE IF NOT EXISTS error_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    error_category_id INT NOT NULL,
    problem_id INT NOT NULL,
    FOREIGN KEY (error_category_id) REFERENCES error_categories(id) ON DELETE CASCADE,
    FOREIGN KEY (problem_id) REFERENCES problems(id) ON DELETE CASCADE
);
