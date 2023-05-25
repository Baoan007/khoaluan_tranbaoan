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
rasa run -m models --enable-api --cors "*" --debug

# rasa run actions
# mở Server thứ 2 để chạy lệnh sau:
rasa run actions
