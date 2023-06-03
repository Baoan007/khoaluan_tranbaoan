from flask import Blueprint
from flask import flash, render_template, jsonify, request, abort, redirect, url_for
from database.models.tuyen_sinh import TuyenSinh
from utils.utils import format_amount
from routes.cors import csrf
import requests
import re
from database.database import db


def get_all_nganh_utils():
    tuyen_sinhs = db.session.query(TuyenSinh).all()
    if tuyen_sinhs:
        message = f"Thông tin tất cả các ngành có sẵn của trường KHTN:"
        for tuyen_sinh in tuyen_sinhs:
            message += f"\n- Mã ngành: {tuyen_sinh.ma_chuyen_nganh}"
            message += f" và Khoa: {tuyen_sinh.ten_nganh}"
        message += "\n Bạn vui lòng nhập đúng ngành để được hỗ trợ."

    return message
