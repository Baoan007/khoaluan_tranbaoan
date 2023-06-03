Bao An Tran
phương án xử lý cho nhập tên ngành không chính xác:
+ giữ nguyên so sánh chính xác tên ngành.
+ trường hợp không tìm thấy thấy tên ngành thì xuất ra: 
    - danh sách toàn bộ mã ngành: ma_nganh + ten_nganh
    - viết thêm utter_nhap_ma_nganh: "vui lòng nhập đúng mã ngành để được hỗ trợ
   - viết 1 action cho ma nganh.


# Story 1. Câu chuyện lấy tất cả ngành và kết hợp với tìm ngành
# Với ---> Khác nếu câu user nhập trùng với intent của rule
http://localhost:5006/visualization.html
user: Chào
---> Khác: 
Tôi cảm thấy rất tốt -> Chạy rule -> 
user: Cho tôi biết tất cả các ngành?
---> Khác:
#(Sử dụng rule)
Tôi rất vui 
---> Chạy rule -> Bot sẽ bảo hỏi tiếp -> 
user: Cho tôi biết tất cả các ngành? |-> lặp lại -> Vẫn trả về response đúng
user: Cho tôi biết tất cả các ngành? |-> lặp lại -> Vẫn trả về response đúng


# Story 2: Câu chuyện sẽ chuyển qua tìm tên ngành
Tiếp tục -> chạy vào giữa story 2
user: Tôi muốn tìm hiểu về ngành [hóa học](ten_nganh) -> Vẫn trả về response đúng -> đã lưu ten_nganh vào slot: slot{"ten_nganh": "Sinh học"} 
Sau đó tôi trở về story 1 ->
user: Cho tôi biết tất cả các ngành? -> Vẫn trả response đúng
Tiếp tục ->
user: Tôi rất vui -> Vẫn trả về rule đúng.
Tiếp tục ->
user: bye -> Vẫn trả về đúng.

user: chào -> action_default_fallback -> (Bị kết thúc session khi đó tôi muốn reset tất cả lại từ đầu khi người dùng đã bye)
... tiếp tục chạy vẫn bình thường nếu đi vào giữa story
user: Cho tôi biết tất cả các ngành? -> Vẫn trả response đúng


