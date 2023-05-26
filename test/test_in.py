from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.models.tuyen_sinh import TuyenSinh
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/my_khtn'
db = SQLAlchemy(app)

# Đường dẫn đến tệp JSON
json_file = 'result.json'

# Đọc tệp JSON và chuyển đổi thành đối tượng Python
with open(json_file, 'r') as f:
    json_data = json.load(f)

print(json_data)

tuyen_sinhs = []
# Duyệt qua từng đối tượng JSON và thêm vào bảng "tuyen_sinh"
for item in json_data:
    ten_nganh = item['Tên ngành']
    khoa = item['Khoa']
    ma_chuyen_nganh = item['Mã chuyên ngành']
    chi_tieu = item['chỉ tiêu']
    hoc_phi_du_kien = 0
    if len(item['Học phí dự kiến']) > 0:
        hoc_phi_du_kien = float(item['Học phí dự kiến'].replace('.', ''))

    tuyen_sinh = TuyenSinh(
        ten_nganh, khoa, ma_chuyen_nganh, chi_tieu, hoc_phi_du_kien)
    tuyen_sinhs.append(tuyen_sinh)

with app.app_context():
    db.session.add_all(tuyen_sinhs)
    db.session.commit()

# db.session.commit()
