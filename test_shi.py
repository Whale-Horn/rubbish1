import csv
import math

#第一题
#定义一个球体类
class Sphere:
#定义私有数据成员半径
    def __init__(self, radius):
        self.__radius = radius

#定义成员方法表面积
    def surface_area(self):
        return 4 * math.pi * self.__radius**2

#定义成员方法体积
    def volume(self):
        return (4/3) * math.pi * self.__radius**3

#定义成员方法修改半径
    def set_radius(self, new_radius):
        self.__radius = new_radius

##定义成员方法重置半径
    def reset_radius(self):
        self.__radius = 0
        
#第二题
# 实例化一个球体，半径为11
my_sphere = Sphere(11)

# 建立两个空列表
surface_area_list = []
volume_list = []

# 获取球体的表面积和体积
surface_area = my_sphere.surface_area()
volume = my_sphere.volume()

# 格式化输出球体的表面积和体积
print("球体半径为{}时的表面积：{:.2f}".format(my_sphere._Sphere__radius, surface_area))
print("球体半径为{}时的体积：{:.2f}".format(my_sphere._Sphere__radius, volume))

#第三题
# 重置球体的半径为 1 到 10，计算并添加表面积和体积到列表
for radius in range(1, 11):
    my_sphere.set_radius(radius)
    surface_area = my_sphere.surface_area()
    volume = my_sphere.volume()
    surface_area_list.append(surface_area)
    volume_list.append(volume)

#第四题
# 写入表面积数据到CSV文件
with open('surface_area.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['球半径', '表面积'])
    for radius, surface_area in zip(range(1, 11), surface_area_list):
        writer.writerow([radius, surface_area])

# 写入体积数据到CSV文件
with open('volume.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['球半径', '体积'])
    for radius, volume in zip(range(1, 11), volume_list):
        writer.writerow([radius, volume])

# 读取表面积数据并格式化输出
with open('surface_area.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    print("表面积数据：")
    for row in reader:
        if row[0] == '球半径':
            continue
        radius = int(row[0])
        surface_area = float(row[1])
        print(f"球半径{radius}的表面积为{surface_area}")

print()

# 读取体积数据并格式化输出
with open('volume.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    print("体积数据：")
    for row in reader:
        if row[0] == '球半径':
            continue
        radius = int(row[0])
        volume = float(row[1])
        print(f"球半径{radius}的体积为{volume}")
