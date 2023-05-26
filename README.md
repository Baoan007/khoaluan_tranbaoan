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

# **\*\***\_**\*\***

- python

# Kết nối rasa

B1. Xây dựng route(API) -> Post(params:{message:'greet'})
B2.

- Không thể train được ra theo ý bạn tại vì đây là bên thứ 3 nó đã đã train bên web nó bạn cái đó bạn đã sử dụng api của nó.

# Chạy rasa javascript

============= Install =============

# Tạo môi trường ảo

python -m venv ./venv

# activate môi trường ảo

.\venv\Scripts\activate

# Upgrade pip

python -m pip install

# install rasa api

pip install rasa

# train rasa để tạo file models

rasa train

============= Các câu lệnh chạy trên server =============

# cho phép các nguồn tài nguyên như html, css, javascript... được truy vấn cùng lúc với các domain khác nhau:

# mở Server thứ 1 để chạy lệnh sau:

rasa run -m models --enable-api --cors "\*" --debug

# rasa run actions

# mở Server thứ 2 để chạy lệnh sau:

rasa run actions

# train rasa -> tạo ra models

# cd rasa && rasa train

# cd rasa && rasa run -m models --enable-api --cors "\*" --debug

# cd rasa run --enable-api --cors "\*"

# cd rasa && rasa run actions
