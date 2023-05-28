from flask import Blueprint
from flask import flash, render_template, jsonify, request, abort, redirect, url_for
from database.models.tuyen_sinh import TuyenSinh
from utils.utils import format_amount
from routes.cors import csrf
import requests
import re
from database.database import db
api_bp = Blueprint('api', __name__)
pattern = r"ngành\s+(.+)"


@api_bp.route('/lay-nganh', methods=['GET'])
@csrf.exempt
def get_nganh():
    # Lấy dữ liệu từ yêu cầu POST
    payload_message = request.args.get('message', '', type=str)
    print(payload_message)
    match = re.search(pattern, payload_message)
    message = ""
    print(payload_message)
    if match:
        ten_nganh = match.group(1).strip().lower()
        print(ten_nganh)
        if ten_nganh:
            tuyen_sinh = db.session.query(
                TuyenSinh).filter_by(ten_nganh=ten_nganh).first()
            print(tuyen_sinh)
            if tuyen_sinh:
                message = f"Thông tin về ngành {tuyen_sinh.ten_nganh}:"
                message += f"\n- Khoa: {tuyen_sinh.khoa}"
                message += f"\n- Mã chuyên ngành: {tuyen_sinh.ma_chuyen_nganh}"
                message += f"\n- Chỉ tiêu: {tuyen_sinh.chi_tieu}"
                message += f"\n- Học phí dự kiến: {format_amount(tuyen_sinh.hoc_phi_du_kien)} vnd"
                return jsonify({"payload": message, "ten_nganh": tuyen_sinh.ten_nganh}), 200
            else:
                message = f"Không tìm thấy thông tin về ngành {ten_nganh}"
                return jsonify({"payload": message}), 400
    print(message)
    message = "Xin lỗi, tôi không thể tìm kiếm thông tin với các thông tin đã cho."
    return jsonify({"payload": message}), 400


@api_bp.route('/lay-chi-tieu-nganh', methods=['GET'])
@csrf.exempt
def get_chi_tieu_nganh():
    # Lấy dữ liệu từ yêu cầu POST
    payload_message = request.args.get('message', '', type=str)
    print(payload_message)
    match = re.search(pattern, payload_message)
    message = ""
    print(payload_message)
    if match:
        ten_nganh = match.group(1).strip().lower()
        print(ten_nganh)
        if ten_nganh:
            tuyen_sinh = db.session.query(
                TuyenSinh).filter_by(ten_nganh=ten_nganh).first()
            print(tuyen_sinh)
            if tuyen_sinh:
                message = f"Thông tin về ngành {tuyen_sinh.ten_nganh}:"

                message += f"\n- Chỉ tiêu: {tuyen_sinh.chi_tieu}"

                return jsonify({"payload": message, "ten_nganh": tuyen_sinh.ten_nganh}), 200
            else:
                message = f"Không tìm thấy thông tin về ngành {ten_nganh}"
                return jsonify({"payload": message}), 400
    print(message)
    message = "Xin lỗi, tôi không thể tìm kiếm thông tin với các thông tin đã cho."
    return jsonify({"payload": message}), 400
