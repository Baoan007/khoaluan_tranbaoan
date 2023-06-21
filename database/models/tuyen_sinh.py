from database.database import db


class TuyenSinh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ten_nganh = db.Column(db.String(1000))
    khoa = db.Column(db.String(100))
    ma_chuyen_nganh = db.Column(db.String(50))
    chi_tieu = db.Column(db.Integer)
    hoc_phi_du_kien = db.Column(db.Float)

    def __repr__(self):
        return f"<TuyenSinh {self.id}>"

    def __init__(self, ten_nganh, khoa, ma_chuyen_nganh, chi_tieu, hoc_phi_du_kien):
        self.ten_nganh = ten_nganh
        self.khoa = khoa
        self.ma_chuyen_nganh = ma_chuyen_nganh
        self.chi_tieu = chi_tieu
        self.hoc_phi_du_kien = hoc_phi_du_kien
