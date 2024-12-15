import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_scoring(user_input):
    """
    OpenAI GPT-4 API에 사용자 입력을 보내고 응답을 받습니다.
    
    Args:
        user_input (str): 사용자의 입력 문장.
    
    Returns:
        str: Chatbot의 응답.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7,  # 응답의 창의성 제어 (0~1)
            max_tokens=500    # 최대 토큰 수 제한
        )
        message = response.choices[0].message['content']
        return message
    except Exception as e:
        return f"오류가 발생했습니다: {e}"
