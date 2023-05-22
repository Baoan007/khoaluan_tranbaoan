
from flask import Flask
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request, abort
import os
from rasa_api import model_path, register_bot_dev, call_rasa_model
from config import app_config
import threading
from rasa.core.agent import Agent
import asyncio
app = Flask(__name__, static_folder="templates")
app.config.from_object(app_config)


@app.route("/chat", methods=["GET"])
def chat():
    # Gọi mô hình Rasa và nhận kết quả trả về
    response =  asyncio.run(call_rasa_model("hi"))
    # response = call_rasa_model("hi")
    print(response)
    # Trả về kết quả dưới dạng JSON
    return response


@app.route('/')
def hello():
    # Xử lí rasa
    # return 'Hello, Flask!'
    return render_template('index.html')


def daemon_thread():
    app.run(port=8000, debug=False)


if __name__ == '__main__':
    if os.getenv('DEBUG') == 'prod':
        # Chạy Thread Flask
        # Từ chối truyền đối số nha, nó sẽ lỗi thread main
        threading.Thread(target=daemon_thread, daemon=True).start()
        print("RUN_THREAD MAIN")
        # Chạy Thread Main Không nên đưa đoạn dưới vào thread vì nó không phù hợp trên server vultr
        register_bot_dev()
    else:
        if app.config['RASA_ENABLE']:
            threading.Thread(target=register_bot_dev, daemon=True).start()
        app.run(port=8000, debug=True)
