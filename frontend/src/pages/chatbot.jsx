import React, { useState } from "react";
import Header from "../components/Header";
import axios from "axios";
import API from "../config/api"; // API URL 가져오기

function Chatbot() {
  const [userInput, setUserInput] = useState(""); // 사용자 입력값
  const [response, setResponse] = useState(""); // GPT의 응답
  const [isLoading, setIsLoading] = useState(false); // 로딩 상태

  // API 호출 함수
  const fetchChatbotResponse = async () => {
    if (!userInput.trim()) return; // 입력값이 비어있으면 실행 X
    setIsLoading(true); // 로딩 상태 시작

    try {
      const res = await axios.post(API.CHATBOT, { user_input: userInput }); // API URL 사용
      setResponse(res.data.response); // GPT 응답 상태에 저장
    } catch (error) {
      console.error("Error fetching chatbot response:", error);
      setResponse("오류가 발생했습니다. 다시 시도해주세요.");
    } finally {
      setIsLoading(false); // 로딩 상태 종료
    }
  };

  // 입력값 변경 핸들러
  const handleInputChange = (e) => {
    setUserInput(e.target.value);
  };

  // 메시지 전송 핸들러
  const handleSubmit = (e) => {
    e.preventDefault();
    fetchChatbotResponse();
  };

  return (
    <div>
      {/* 상단 헤더 */}
      <Header />

      {/* 채팅 컨테이너 */}
      <div style={styles.container}>
        <h2>토픽 챗봇</h2>
        <p>GPT-4 기반 토픽 챗봇과 채팅해보세요!</p>

        {/* 입력 폼 */}
        <form onSubmit={handleSubmit} style={styles.form}>
          <input
            type="text"
            value={userInput}
            onChange={handleInputChange}
            placeholder="질문을 입력하세요..."
            style={styles.input}
          />
          <button type="submit" style={styles.button} disabled={isLoading}>
            {isLoading ? "전송 중..." : "전송"}
          </button>
        </form>

        {/* GPT 응답 출력 */}
        {response && (
          <div style={styles.responseBox}>
            <h3>GPT 응답:</h3>
            <p>{response}</p>
          </div>
        )}
      </div>
    </div>
  );
}

// 인라인 스타일 정의
const styles = {
  container: {
    maxWidth: "600px",
    margin: "20px auto",
    padding: "20px",
    backgroundColor: "#f9f9f9",
    borderRadius: "8px",
    boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
    textAlign: "center",
  },
  form: {
    display: "flex",
    justifyContent: "center",
    marginTop: "20px",
  },
  input: {
    flex: "1",
    padding: "10px",
    fontSize: "1rem",
    border: "1px solid #ccc",
    borderRadius: "4px",
    marginRight: "10px",
  },
  button: {
    padding: "10px 15px",
    fontSize: "1rem",
    color: "#fff",
    backgroundColor: "#4CAF50",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
  },
  responseBox: {
    marginTop: "20px",
    padding: "15px",
    backgroundColor: "#fff",
    border: "1px solid #ddd",
    borderRadius: "4px",
    textAlign: "left",
    whiteSpace: "pre-wrap", // 줄바꿈 처리
  },
};

export default Chatbot;
