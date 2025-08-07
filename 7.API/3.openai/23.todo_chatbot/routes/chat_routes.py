from flask import Blueprint, request, jsonify
from services import chat_service as svc

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/', methods=['POST'])
def chatbot_response():
    userInput = request.get_json()['userInput']
    print('사용자 입력값 :', userInput)

    result = svc.handle_chatgpt(userInput)

    return jsonify({'response': f'[BOT] {result}'})

