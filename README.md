# khoaluan_tranbaoan

Khóa luận tuyển sinh đại học.

# Các cứu pháp chạy project

# Chạy trên nền python 3.8

python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Cập nhật thêm thư viện rasa machine learning -(Không cần cập nhật vì chưa dùng đến)

pip install -r requirements_u.txt
pip install -U 'rasa[spacy]'
spacy download en_core_web_lg

nohup python app.py

# Cấu trúc thư mục

- Chạy từ hàm app.py -> khi chạy server thì chạy file này

- Các file config -> Thêm các biến config nhớ thay đổi thành prod nếu up lên server

- File env -> Lưu trữ các thông tin mật về môi trường phát triển

# SSH

ssh root@45.32.29.231
Rj7@{=TNK4DN)j@T

cd .. &&cd home/khtntuyensinh.autos&&source env/bin/activate&&nohup python app.py

# Phần config nginx - (Không cần quan tâm phần này)

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

**\*\***\_**\*\*** Hướng dẫn cơ bản rasa \***\*\_\*\***

# train rasa -> tạo ra models

# Mỗi khi thay đổi 1 gì đó trong các file của rasa phải train lại

Kiểm tra xem có lỗi trước khi train hay không
rasa data validate
Chạy generate ra models
rasa train

# Cứu pháp chạy rasa**\_**

# Cứu pháp debug

rasa run -m models --enable-api --cors "\*" --debug

# Cứu pháp rút gọn

rasa run --enable-api --cors "\*"

# Chạy action custom**\_\_**

rasa run actions

# only Train nlu

rasa train nlu

# Chạy trên terminal

rasa shell --debug

# Chọn menu interactive khi chạy hết story

ctrl+C -> chọn start session

# Thông tin database trên server

Thong tin:
PhpMyAdmin: http://45.32.29.231:6789/phpmyadmin
Auth_Username: admin
Auth_Password: NDllNTQ4NGNmOWFjYWEzZmU5NWE3YTY5
DB_User: admin_larvps
DB_Password: Mzc1Y2IyOTA2Yzc5M2IwYWUxM2ZlODM3

# Chạy lên server

nohup rasa run actions&nohup rasa run -m models --enable-api --cors "\*" &nohup python app.py

# Tất cả port để chạy

- 5005 - entrypoint
- 5055 - socket
- 8000 - flask

# Cấu hình trên Vultr server

Chạy port 5005
rasa run -m models --enable-api --cors "\*" --port 5005 --config config.yml
