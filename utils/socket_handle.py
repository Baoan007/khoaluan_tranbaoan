from flask_socketio import emit
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action


class SocketHandler(BaseNamespace):
    def on_connect(self):
        print('Client connected')

    def on_disconnect(self):
        print('Client disconnected')

    def on_user_uttered(self, data):
        message = data['message']
        sender_id = data['sender_id']

        # Truyền dữ liệu từ người dùng đến Rasa và nhận phản hồi từ Rasa
        dispatcher = CollectingDispatcher()
        # response = agent.handle_text(message, sender_id, dispatcher)
        response = {'hi': 'hi'}
        # Gửi phản hồi từ Rasa về cho người dùng qua SocketIO
        emit('bot_uttered', {'message': response}, room=sender_id)
