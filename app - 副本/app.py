from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

# 定义数据库文件路径
#DB_PATH = "C:\\Users\\ASUS\\Desktop\\app\\database.db"

import os

# 获取当前脚本文件所在目录的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

#解决跨域资源共享（CORS）问题
@app.after_request
def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# 初始化数据库表
def initialize_database():
    # 连接到数据库
    conn = sqlite3.connect(DB_PATH)
    # 创建游标
    c = conn.cursor()
    # 执行创建表的SQL语句
    c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, id_number TEXT, major TEXT, name TEXT, dorm_location TEXT)')
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()

@app.route('/open')
def home():
    return render_template('test.html')

# 获取所有数据
@app.route('/data', methods=['GET'])
def get_all_data():
    # 连接到数据库
    conn = sqlite3.connect(DB_PATH)
    # 创建游标
    c = conn.cursor()
    # 执行查询语句，检索表中的所有数据
    c.execute('SELECT * FROM data')
    # 获取查询结果
    data = c.fetchall()
    # 关闭数据库连接
    conn.close()
    # 返回包含所有数据的JSON响应
    return jsonify(data)

# 根据id获取数据
@app.route('/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    # 连接到数据库
    conn = sqlite3.connect(DB_PATH)
    # 创建游标
    c = conn.cursor()
    # 执行查询语句，根据id获取数据
    c.execute('SELECT * FROM data WHERE id = ?', (data_id,))
    # 获取查询结果的第一行数据
    data = c.fetchone()
    # 关闭数据库连接
    conn.close()
    # 判断是否找到数据
    if data:
        # 返回包含数据的JSON响应
        return jsonify(data)
    else:
        # 返回数据未找到的JSON响应
        return jsonify({'message': 'Data not found'})

# 添加数据
@app.route('/data', methods=['POST'])
def add_data():
    # 从请求中获取JSON数据
    new_data = request.get_json()
    # 连接到数据库
    conn = sqlite3.connect(DB_PATH)
    # 创建游标
    c = conn.cursor()
    # 执行插入语句，向data表中插入新数据
    c.execute('INSERT INTO data (id_number, major, name, dorm_location) VALUES (?, ?, ?, ?)', (new_data['id_number'], new_data['major'], new_data['name'], new_data['dorm_location']))
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()
    # 返回添加数据成功的JSON响应
    return jsonify({'message': 'Data added successfully'})

# 根据身份证号获取其他三个值
@app.route('/data/id_number/<string:id_number>', methods=['GET'])
def get_data_by_id_number(id_number):
    # 连接到数据库
    conn = sqlite3.connect(DB_PATH)
    # 创建游标
    c = conn.cursor()
    # 执行查询语句，根据身份证号获取数据
    c.execute('SELECT major, name, dorm_location FROM data WHERE id_number = ?', (id_number,))
    # 获取查询结果的第一行数据
    data = c.fetchone()
    # 关闭数据库连接
    conn.close()
    # 判断是否找到数据
    if data:
        # 返回包含数据的JSON响应
        return jsonify({'major': data[0], 'name': data[1], 'dorm_location': data[2]})
    else:
        # 返回数据未找到的JSON响应
        return jsonify({'message': 'Data not found'})

# 访问计数器变量
db_access_count = 0

# 统计数据库访问次数的路由
@app.route('/stats', methods=['GET'])
def get_db_access_count():
    global db_access_count
    # 将访问计数器加一
    db_access_count += 1
    # 构造返回的字符串
    message = f'您是第{db_access_count}位报到的学生，欢迎来到河北医科大学！'
    # 返回构造的字符串
    return message

# 启动服务器
if __name__ == '__main__':
    initialize_database()
    app.run(host='0.0.0.0')
