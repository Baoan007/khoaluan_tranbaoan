
from flask import request, jsonify
from flask import Flask
# from flask_cors import CORS
from flask import Flask, render_template, jsonify, request, abort, jsonify
import os
# from rasa_api import register_bot_dev, call_rasa_model
from config import app_config
import threading
import asyncio
# Database
from database.database import db, migrate, register_db
from rasa_sdk import Action, Tracker

# Đăng kí migrate
from database.migrate import register_migrate_db
from flask_cors import CORS
from routes.cors import register_cors
from utils.socket import register_socket, socketio
from flask_wtf.csrf import CSRFProtect, generate_csrf
from routes.cors import csrf

app = Flask(__name__, static_folder="templates")
app.config.from_object(app_config)


# Đăng kí database và migration
register_db(app)

# Đăng kí migrate trong dabase
register_migrate_db()

# Register cors
register_cors(app)

# Register socket
register_socket(app)

# @app.route("/chat", methods=["GET"])
# def chat():

#     # Gọi mô hình Rasa và nhận kết quả trả về
#     response = asyncio.run(call_rasa_model("greet"))
#     # response = call_rasa_model("hi")
#     print(response)
#     # Trả về kết quả dưới dạng JSON
#     return jsonify(json.dumps(response), 200)


# Endpoint để nhận yêu cầu từ Rasa Server
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    action_name = data['next_action']
    tracker_dict = data['tracker']

    # Tạo đối tượng Tracker từ dữ liệu nhận được
    tracker = Tracker.from_dict(tracker_dict)

    # Tạo đối tượng CollectingDispatcher để gửi phản hồi cho người dùng
    dispatcher = CollectingDispatcher()

    # Gọi Action tương ứng
    action = get_action(action_name)
    action.run(dispatcher, tracker, {})

    # Lấy các phản hồi đã thu thập được
    responses = dispatcher.messages

    # Trả về phản hồi cho Rasa Server
    return jsonify(responses)

# Hàm helper để lấy Action từ tên Action


def get_action(action_name):
    if action_name == 'action_get_chitieu_nganh':
        return GetChitieuNganhAction()

# Action để lấy chỉ tiêu ngành


class GetChitieuNganhAction(Action):
    def name(self):
        return "action_get_chitieu_nganh"

    def run(self, dispatcher, tracker, domain):
        nganh = tracker.get_slot('nganh')

        # Truy vấn cơ sở dữ liệu để lấy chỉ tiêu của ngành
        # code truy vấn cơ sở dữ liệu ở đây

        # Gửi phản hồi cho người dùng
        dispatcher.utter_message(text=f"Chỉ tiêu ngành {nganh} là X")

        return []


@app.route('/')
def index():
    # Xử lí rasa
    # return 'Hello, Flask!'
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404


# @app.route('/socket.io/')
# def socketio_endpoint():
#     # Forward the request to Rasa
#     # socketio_manage(request.environ, {'/socket.io': SocketHandler}, app=app)
#     return 'OK'


@socketio.on('connect')
@csrf.exempt
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
@csrf.exempt
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    # socketio.run(app, debug=True)
    if os.getenv('DEBUG') == 'prod':
        # if app.config['RASA_ENABLE']:
        #     threading.Thread(target=register_bot_dev, daemon=True).start()
        app.run(port=8000, debug=False)
    else:
        # if app.config['RASA_ENABLE']:
        #     threading.Thread(target=register_bot_dev, daemon=True).start()
        app.run(port=8000, debug=True)
