import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)
def write_profreading(problem, answer):
    """
    OpenAI GPT-4o-mini 모델을 사용하여 TOPIK 쓰기 문제를 첨삭하는 함수.
    
    Args:
        problem (str): TOPIK 쓰기 문제.
        answer (str): 사용자의 답변.
    
    Returns:
        str: GPT-4o-mini의 응답.
    """
    try:
        # 시스템 프롬프트 지침 추가
        system_instructions = (
            "TOPIK(한국어 능력시험) 쓰기 문제를 첨삭해주는 도우미 역할을 수행합니다. "
            "TOPIK 문제와 상관 없는 답변이 온다면 'TOPIK 관련한 문제를 제공해주세요' 라는 답변을 해주세요. "
            "문제에서 요구한 과제를 모두 수행하고, 내용이 풍부하게 표현되었는지 평가하세요. "
            "문장은 도입-전개-마무리 구조를 갖추고 있는지 확인하고, 문단 전환이 적절한지 판단합니다. "
            "중고급 수준의 어휘와 문법이 사용되었는지 점검하며, 구어체나 '-요'로 끝나는 표현이 사용되었다면 감점 요소로 언급하세요. "
            "문장이 개조식으로 작성되지 않았는지 확인하고, 글의 형식성과 격식성을 고려하여 평가합니다. "
            "만약 입력 내용이 TOPIK 쓰기 문제와 관련 없는 경우에는 응답하지 않고 무시하세요."
            "답변은 수정해야할 문장 : (수정해야할 문장) \n 수정 사항 : (수정사항) 의 형태로 제공해주세요"
            "수정해야할 문장 하나당 문장 :, 수정 사항: 의 구조로 만들어줘, 여러 문장을 한 번에 수정하려 하지마"
            "수정 사항에서 수정해야할 문장을 직접적으로 언급하며 수정해야할 부분을 짚어줘"
            "문장은 단답형으로 제공해주세요 예시 : 수정해야한다, 올바른 형태로 작성해야한다."
        )

        # 문제와 답변을 구성해 모델에 전달
        user_input_combined = f"문제: {problem}\n답변: {answer}"

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
