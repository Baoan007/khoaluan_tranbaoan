# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models.tuyen_sinh import TuyenSinh
from utils.utils import format_amount

# Kết nối tới cơ sở dữ liệu
engine = create_engine('mysql+pymysql://root:@localhost/my_khtn')
Session = sessionmaker(bind=engine)
session = Session()
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/my_khtn'
# db = SQLAlchemy(app)


def action():
    # with app.app_context():
    nganh = "Sinh học"
    result = session.query(
        TuyenSinh).filter_by(ten_nganh=nganh).first()
    print("hello")
    print(result)
    message = f"Thông tin về ngành {result.ten_nganh}:"
    message += f"\n- Khoa: {result.khoa}"
    message += f"\n- Mã chuyên ngành: {result.ma_chuyen_nganh}"
    message += f"\n- Chỉ tiêu: {result.chi_tieu}"
    message += f"\n- Học phí dự kiến: {format_amount(result.hoc_phi_du_kien)} vnd"
    print(message)


action()
