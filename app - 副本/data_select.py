import requests

# 目标URL
url = 'http://192.168.2.39:5000/data/id_number/123'

# 替换为实际的主机名、端口号和身份证号
hostname = 'localhost'
port = 5000
id_number = '身份证号'

# 格式化URL
url = url.replace('<hostname>', hostname).replace('<port>', str(port)).replace('<id_number>', id_number)

def get_data_by_id_number():
    try:
        # 发送GET请求
        response = requests.get(url)
        
        # 如果返回状态码为200，则请求成功
        if response.status_code == 200:
            data = response.json()
            if 'message' in data:
                print(data['message'])
            else:
                print('专业:', data['major'])
                print('姓名:', data['name'])
                print('宿舍地址:', data['dorm_location'])
        else:
            print('请求失败:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('请求异常:', e)

# 调用函数获取并处理数据
get_data_by_id_number()
