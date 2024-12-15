import openai
from dotenv import load_dotenv
import os
import re

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_scoring(problem, answer):
    """
    OpenAI GPT-4 API에 사용자 입력을 보내고 응답을 점수만 출력하도록 필터링합니다.
    
    Args:
        problem (str): 문제 설명.
        answer (str): 사용자 답변.
    
    Returns:
        str: 점수 (숫자만 반환).
    """
    try:
        system_instructions = (
            "당신은 TOPIK(한국어능력시험) 쓰기 문제를 평가하는 평가위원입니다. "
            "당신은 국어국문학과 교수 수준의 전문성을 가지고 있으며, 답안을 평가해서 평점을 매겨야합니다."
            "\n\n[평가기준]: "
            "- **내용 및 과제 수행**: 주어진 과제를 충실히 수행하였는가? "
            "- 주제에 관련된 내용으로 구성하였는가? "
            "- 주어진 내용을 풍부하고 다양하게 표현하였는가? "
            "\n- **글의 전개 구조**: 글의 구성이 명확하고 논리적인가? "
            "- 글의 내용에 따라 단락 구성이 잘 이루어졌는가? "
            "- 논리 전개에 도움이 되는 담화 표지를 적절하게 사용하여 조직적으로 연결하였는가? "
            "\n- **언어 사용**: 문법과 어휘를 다양하고 풍부하게 사용하였는가? "
            "- 문법, 어휘, 맞춤법 등의 사용이 정확한가? "
            "- 글의 목적과 기능에 따라 격식에 맞게 글을 작성하였는가? "
            "\n\n[지시사항]: "
            "- 답안을 평가 기준에 따라 **50점 만점**으로 평가하세요. "
            "- 평가 결과를 점수와 함께 설명하며, 각 평가 항목에 대한 근거를 명확히 제공하세요. "
            "- 글의 흐름과 문장 구조를 세부적으로 평가하고 논리적 오류나 언어적 실수를 지적하세요. "
            "- 단계별로 생각하며 평가를 진행하세요. (Think step by step)"
            "- 만약 입력된 답변이 TOPIK 쓰기 문제와 관련이 없다면, 0점으로 출력해주세요."
            "점수를 제외한 다른 메시지는 출력하지마세요."
            "\n\n[답변 형식]: "
            "45/50"
        )
        user_input_combined = f"문제: {problem}\n답변: {answer}"
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': system_instructions},
                {'role': 'user', 'content': user_input_combined}
            ],
            temperature=1.0,
            max_tokens=1000,
            top_p=1.0,
            presence_penalty=0.0,
            frequency_penalty=0.0
        )
        raw_output = response.choices[0].message.content

        # 점수만 추출
        score_match = re.search(r"^\d{1,2}/50", raw_output)
        if score_match:
            return score_match.group()
        else:
            return "응답에서 점수를 추출할 수 없습니다."
    except Exception as e:
        return f"오류가 발생했습니다: {e}"
