# khoaluan_tranbaoan

Khóa luận tuyển sinh đại học.

# Các cứu pháp chạy project

# Chạy trên nền python 3.8

python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

nohup python app.py

# Cấu trúc thư mục

- Chạy từ hàm app.py -> khi chạy server thì chạy file này

- Các file config -> Thêm các biến config nhớ thay đổi thành prod nếu up lên server

- File env -> Lưu trữ các thông tin mật về môi trường phát triển

# SSH

ssh root@45.32.29.231
Rj7@{=TNK4DN)j@T

cd .. &&cd home/khtntuyensinh.autos&&source env/bin/activate&&nohup python app.py

cd .. &&cd etc/nginx/

sudo systemctl nginx start
sudo systemctl nginx stop
sudo systemctl nginx restart
systemctl status nginx.service

sudo systemctl start nginx
sudo systemctl restart nginx
