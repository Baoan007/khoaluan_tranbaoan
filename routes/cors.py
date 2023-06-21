from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import request
from flask_cors import CORS

csrf = CSRFProtect()


def register_cors(app):

    # Cấu hình CORS
    csrf.init_app(app)
    CORS(app, origins=['http://127.0.0.1:8000', 'http://localhost:5055', 'http://localhost:5005', 'http://127.0.0.1:5000', 'http://khtntuyensinh.autos',
         'http://khtntuyensinh.info', 'http://0.0.0.0:5055', 'http://45.32.29.231', 'http://localhost:5005'])
