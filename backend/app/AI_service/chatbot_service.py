import openai
from dotenv import load_dotenv
import os

load_dotenv()


client = openai.OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)
def get_chatbot_response(user_input):
    try:
        # 시스템 프롬프트 지침 추가
        system_instructions = (
            "TOPIK(한국어 능력시험) 쓰기 문제를 첨삭해주는 도우미 역할을 수행합니다. "
        )
        
        user_input_combined = user_input
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': system_instructions},
                {'role': 'user', 'content': user_input_combined}
            ],
            temperature=1.0,  # (기본값: 1.0) 응답의 창의성 수준을 결정 (0.0~2.0)
            top_p=1.0,        # (기본값: 1.0) Nucleus Sampling을 사용하여 높은 확률 토큰만 포함 (0.0~1.0)
            max_tokens=1000,  # (기본값: 1000) 생성할 최대 토큰 수
            presence_penalty=0.0,  # (기본값: 0.0) 새로운 주제에 대한 응답을 더 선호하게 함 (-2.0~2.0)
            frequency_penalty=0.0  # (기본값: 0.0) 반복되는 단어 사용을 억제 (-2.0~2.0)
        )
        # 응답 내용
        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        return f"에러가 발생했습니다: {e}"
