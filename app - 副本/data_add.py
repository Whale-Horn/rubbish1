import sqlite3

def insert_data(id_number, major, name, dorm_location):
    # 连接到数据库
    conn = sqlite3.connect("database.db")
    # 创建游标
    c = conn.cursor()
    # 执行插入语句，向data表中插入新数据
    c.execute('INSERT INTO data (id_number, major, name, dorm_location) VALUES (?, ?, ?, ?)', (id_number, major, name, dorm_location))
    # 提交事务
    conn.commit()
    # 关闭数据库连接
    conn.close()

# 调用函数插入数据
insert_data("130533200302012737", "21级智能医学工程", "胡开帅", "仲景园708")
