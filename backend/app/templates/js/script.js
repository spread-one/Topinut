// API URL 정의
const API_URL = "https://example.com/api/chatbot"; // 여기에 실제 API URL을 넣으세요

// DOM 요소 가져오기
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const submitButton = document.getElementById('submit-button');
const responseBox = document.getElementById('response-box');
const responseText = document.getElementById('response-text');

// 전송 버튼의 상태를 설정하는 함수
const setButtonLoadingState = (isLoading) => {
    submitButton.disabled = isLoading;
    submitButton.textContent = isLoading ? '전송 중...' : '전송';
};

// API 호출 함수
const fetchChatbotResponse = async () => {
    const userInputValue = userInput.value.trim();
    if (!userInputValue) return; // 입력값이 비어 있으면 종료

    setButtonLoadingState(true); // 로딩 상태로 설정

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userInputValue }),
        });

        const data = await response.json();

        if (response.ok) {
            // 성공적으로 응답 받음
            responseText.textContent = data.response || '응답이 없습니다.';
            responseBox.classList.remove('hidden');
        } else {
            // 오류 메시지 표시
            responseText.textContent = '서버 오류가 발생했습니다. 다시 시도해주세요.';
            responseBox.classList.remove('hidden');
        }
    } catch (error) {
        console.error('Error:', error);
        responseText.textContent = '네트워크 오류가 발생했습니다.';
        responseBox.classList.remove('hidden');
    } finally {
        setButtonLoadingState(false); // 로딩 종료
    }
};

// 폼 전송 핸들러
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    fetchChatbotResponse();
});
