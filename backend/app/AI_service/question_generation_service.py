import openai
from dotenv import load_dotenv
import os

load_dotenv()

# OpenAI API 클라이언트 초기화
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
def format_response_with_line_breaks(text):
    """
    텍스트를 문장 단위로 나누어 줄바꿈 추가
    """
    import re
    # 정규 표현식으로 문장 끝(마침표, 물음표, 느낌표) 뒤에 줄바꿈 추가
    formatted_text = re.sub(r'([.!?])\s+', r'\1\n', text.strip())
    return formatted_text

def get_question_generation():
    try:
        # 시스템 프롬프트 지침
        system_instructions = (
            "당신은 TOPIK2의 쓰기영역 작문형 54번 문항 출제 위원입니다.\n\n"
            "54번 문항은 600-700자 정도의 고급 수준 논술문입니다.\n\n"
            "TOPIK은 외국인을 비롯한 한국어를 모어로 하지 않는 사람들을 대상으로 한 한국어능력시험입니다.\n\n"
            "[평가기준]:\n"
            "- **내용 및 과제 수행**: 주어진 과제를 충실히 수행하였는가?\n"
            "- **글의 전개 구조**: 글의 구성이 명확하고 논리적인가?\n"
            "- **언어사용**: 문법과 어휘를 정확하고 다양하게 사용하였는가?\n\n"
            "[지시사항]:\n"
            "1. 한국어 글쓰기 능력을 평가하기 위한 600-700자 논술문 문제 1개를 디자인합니다.\n"
            "2. 각 문제는 50자 이내의 주제문과 3가지 질문으로 이루어져야 합니다.\n"
            "3. 문제의 난이도는 TOPIK 54번 수준으로 출제되어야 합니다.\n"
            "\n[문제 예시]:\n"
            "**주제:** 사람은 누구나 청소년기를 거쳐 어른이 된다. 청소년기의 중요성에 대해 작성하시오.\n"
            "- 청소년기가 중요한 이유는 무엇인가?\n"
            "- 청소년들은 이 시기에 주로 어떤 특징을 보이는가?\n"
            "- 청소년의 올바른 성장을 돕기 위해 어떤 노력이 필요한가?"
            "문제는 하나만 생성해야합니다."
            "문장마다 줄바꿈을 진행해주세요."
            "600자-700자로 작성해야한다고 명시해야합니다."
        )

        # 사용자 입력
        user_input_combined = "문제를 하나 생성해주세요 문장마다 줄바꿈을 꼭 해주세요"

        # GPT-4 API 호출
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": user_input_combined}
            ],
            temperature=1.5,  # 창의성 증가
            top_p=1.0,
            max_tokens=1000,
            presence_penalty=0.5,
            frequency_penalty=0.5
        )

        # 응답 내용 반환
        reply = response.choices[0].message.content.strip()
        # 문장 단위 줄바꿈 적용
        formatted_reply = format_response_with_line_breaks(reply)
        return formatted_reply

    except Exception as e:
        return f"에러가 발생했습니다: {e}"
