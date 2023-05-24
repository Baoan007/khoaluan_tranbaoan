from rasa.core.agent import Agent
import os
import asyncio

current_dir = os.path.abspath(os.getcwd())
# Đường dẫn tới thư mục chứa mô hình đã được huấn luyện
model_path = current_dir+"/rasa/models/core-20230518-091442-angry-resin.tar.gz"
# Khởi tạo mô hình Rasa
global agent


async def call_rasa_model(data):
    global agent
    # Trích xuất thông tin từ yêu cầu

    message = data
    json_response = {
        'message': 'Mô hình chưa được tải lên'
    }
    if 'agent' in globals():
        if agent:
            # Gửi tin nhắn tới mô hình Rasa để nhận phản hồi
            # Do đây là coroutine (Bất đồng bộ) nên phải dùng await để xử lí và dùng asyncio để chạy bất đồng bộ python
            response = await agent.handle_text(message)
            print(response)
            if len(response) > 0:
                # Trích xuất phản hồi từ kết quả trả về của mô hình
                text_response = response[0]['text']
                print("Kết quả trích xuất thông tin từ mô hình")
                print(text_response)
                # Tạo đối tượng JSON response
                json_response = {
                    'response': text_response,
                    'message': 'Đã trích xuất dữ liệu từ mô hình thành công'
                }

    return json_response


def register_bot_dev():
    global agent
    agent = Agent.load(model_path)

    # Kiểm tra xem mô hình đã tải thành công hay chưa
    if agent:
        print("Mô hình đã được tải thành công!")
    else:
        print("Không thể tải mô hình.")
