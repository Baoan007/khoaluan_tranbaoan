
from flask import request, jsonify
from flask import Flask
from flask import Flask, render_template, jsonify, request, abort, jsonify
import os
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
from flask_wtf.csrf import CSRFProtect, generate_csrf
from routes.cors import csrf
from routes.blueprint import register_blueprints

app = Flask(__name__, static_folder="templates")
app.config.from_object(app_config)


# Đăng kí database và migration
register_db(app)

# Đăng kí migrate trong dabase
register_migrate_db()

# Register cors
register_cors(app)

# Cấu hình app
register_blueprints(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404


if __name__ == '__main__':
    if os.getenv('DEBUG') == 'prod':
        app.run(port=8000, debug=False)
    else:
        app.run(port=8000, debug=True)
