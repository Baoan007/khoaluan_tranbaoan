
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
@csrf.exempt
def index():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('index.html', payload=payload)


@app.route('/dao-tao')
@csrf.exempt
def daotao():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('daotao.html', payload=payload)


@app.route('/chi-tieu')
@csrf.exempt
def chitieu():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('chitieu.html', payload=payload)


@app.route('/hoc-phi')
@csrf.exempt
def hocphi():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('hocphi.html', payload=payload)


@app.route('/huong-dan-nhap-hoc')
@csrf.exempt
def huongdannhaphoc():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('huongdannhaphoc.html', payload=payload)


@app.route('/nganh-dao-tao')
@csrf.exempt
def nganhdaotao():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('nganhdaotao.html', payload=payload)


@app.route('/phuong-thuc-tuyen-sinh')
@csrf.exempt
def phuongthuctuyensinh():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('phuongthuctuyensinh.html', payload=payload)


@app.route('/to-hop-tuyen-sinh')
@csrf.exempt
def tohoptuyensinh():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('tohoptuyensinh.html', payload=payload)


@app.route('/tuyen-sinh')
@csrf.exempt
def tuyensinh():
    payload = {
        "domain": app_config.DOMAIN,
        "domain_socket": app_config.DOMAIN_SOCKET
    }
    return render_template('tuyensinh.html', payload=payload)


@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404


if __name__ == '__main__':
    if os.getenv('DEBUG') == 'prod':
        app.run(port=8000, debug=False)
    else:
        app.run(port=8000, debug=True)
