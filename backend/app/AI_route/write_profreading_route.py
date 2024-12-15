from flask import Flask, request, jsonify
from AI_service.write_profreading_service import write_profreading

app = Flask(__name__)

@app.route('/api/write_profreading', methods=['POST'])
def gpt_response():
    """
    OpenAI GPT-4o-mini를 사용한 TOPIK 문제 첨삭 API.

    Request:
        - JSON 데이터: {"problem": "<문제>", "answer": "<답변>"}
    
    Response:
        - JSON 데이터: {"result": "<GPT 응답>"}
    """
    try:
        # 클라이언트에서 전달된 데이터 추출
        data = request.get_json()
        problem = data.get("problem")
        answer = data.get("answer")

        # 입력 값 검증
        if not problem or not answer:
            return jsonify({"error": "문제와 답변을 모두 입력해주세요"}), 400

        # OpenAI API 호출
        result = write_profreading(problem, answer)

        # 결과 반환
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": f"에러가 발생했습니다: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
