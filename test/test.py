import pandas as pd
import json

# Đường dẫn đến file Excel
excel_file = 'tuyen_sinh_data.xlsx'

# Đọc file Excel vào DataFrame
df = pd.read_excel(excel_file)

# Chuyển đổi DataFrame thành mẫu JSON
json_data = df.to_json(orient='records')

# In ra mẫu JSON
print(json_data)
json_data_loads = json.loads(json_data)

# Tên tệp JSON xuất ra
output_file = 'result.json'

# Ghi mẫu JSON vào tệp JSON
with open(output_file, 'w') as f:
    # json.dump(json_data, f)
    json.dump(json_data_loads, f)

# .encode(
#     'utf-8').decode('unicode-escape')
print(f"Đã xuất dữ liệu thành công vào tệp {output_file}.")
