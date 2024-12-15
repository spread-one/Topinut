import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def export_category(input):
    try:
        # 시스템 프롬프트 지침 추가
        system_instructions = (
            "너는 TOPIK(한국어능력시험) 전문가로써 업무를 보조해주는 역할을 합니다. "
            "당신은 국어국문학과 교수 수준의 전문성을 가지고 있습니다. "
            "입력으로 들어온 이미 첨삭된 데이터를 바탕으로 틀린 부분의 카테고리를 지정합니다. "
            "틀린 부분의 카테고리는 아래와 같아: "
            "맞춤법 오류, 문법 오류, 조사 오류, 높임말 오류, 어순 오류, 의미 중복 오류, 부사 사용 오류, 동사 활용 오류, 명사 사용 오류, 형용사 사용 오류, 문장 연결 오류, 구두점 오류, 텍스트 일관성 오류, 대명사 사용 오류, 고유명사 표기 오류, 불필요한 반복 오류, 접속사 사용 오류, 생략 오류, 문장 분리 오류, 문체 오류. "
            "출력은 다음과 같은 형식으로 제공해야합니다: "
            "[{\"category_name\": \"맞춤법 오류\", \"increment\": 3}, {\"category_name\": \"문법 오류\", \"increment\": 1}, {\"category_name\": \"조사 오류\", \"increment\": 4}, {\"category_name\": \"높임말 오류\", \"increment\": 2}, {\"category_name\": \"어순 오류\", \"increment\": 1}] "
            "위와 같은 형식으로 category_name과 increment 값을 정확히 제공합니다. "
            "category_name은 반드시 위에 제공된 목록 중 하나여야 하며, increment는 양의 정수로 입력합니다."
        )

        user_input_combined = input

        # OpenAI API 호출
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': system_instructions},
                {'role': 'user', 'content': user_input_combined}
            ],
            temperature=1.0,
            max_tokens=3000,
            top_p=1.0,
            presence_penalty=0.0,
            frequency_penalty=0.0
        )

        # 응답 내용 반환
        return response.choices[0].message.content

    except Exception as e:
        # 에러 처리
        return f"에러가 발생했습니다: {e}"
