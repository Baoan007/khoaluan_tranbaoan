
from flask import Flask
# from flask_cors import CORS
from flask import Flask, render_template, jsonify, request, abort, jsonify
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
    response = asyncio.run(call_rasa_model("greet"))
    # response = call_rasa_model("hi")
    print(response)
    # Trả về kết quả dưới dạng JSON
    return jsonify(response, 200)


@app.route('/')
def hello():
    # Xử lí rasa
    # return 'Hello, Flask!'
    return render_template('index.html')


if __name__ == '__main__':
    if os.getenv('DEBUG') == 'prod':
        if app.config['RASA_ENABLE']:
            threading.Thread(target=register_bot_dev, daemon=True).start()
        app.run(port=8000, debug=False)
    else:
        if app.config['RASA_ENABLE']:
            threading.Thread(target=register_bot_dev, daemon=True).start()
        app.run(port=8000, debug=True)
