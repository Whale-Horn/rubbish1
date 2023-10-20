import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# 获取数据集
def get_data():
    iris = load_iris()
    return iris.data, iris.target

# 划分数据集为训练集和测试集
def split_data(data, target):
    # 转换为NumPy数组
    data = np.array(data)
    target = np.array(target)
    target = np.reshape(target, (target.shape[0], 1))

    # 数据正则化
    sd = StandardScaler()
    data = sd.fit_transform(data)

    # 拼接特征值和类别
    dataset = np.hstack((data, target))
    n = dataset.shape[0]

    # 打乱数据
    np.random.shuffle(dataset)

    # 划分数据集，返回训练集和测试集
    train = dataset[:int(0.7 * n), :]
    test = dataset[int(0.7 * n):, :]

    return train, test

# sigmoid函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 画出sigmoid函数曲线
def draw_sigmoid():
    fig, ax = plt.subplots()
    x_data = np.arange(-10, 10, 0.1)
    ax.plot(x_data, sigmoid(x_data))
    plt.show()

# 计算代价函数
def calCost(dataset, theta):
    x = dataset[:, :-1]
    y = dataset[:, -1:]
    z = x @ theta.T
    m = y.size # 训练数据个数，也可以用m = y.shape[1]
    para1 = np.multiply(-y, np.log(sigmoid(z)))
    para2 = np.multiply((1 - y), np.log(1 - sigmoid(z)))
    J = 1 / m * np.sum(para1 - para2) # 代价函数J
    return J

# 梯度下降算法
def gradient(dataset, theta, iters, alpha):
    x = dataset[:, :-1]
    y = dataset[:, -1:]
    for i in range(iters):
        h_x = sigmoid(x @ theta.T)
        theta = theta - alpha / len(x) * (h_x - y).T @ x
    return theta

# 返回第i类的数据
def get_per_classify_data(data, i):
    return data[data[:, -1] == i]

# 获取每个类别的theta值
def get_final_theta(data, i, theta, iters, alpha):
    dataset = get_per_classify_data(data, i)
    return gradient(dataset, theta, iters, alpha)

# 预测结果
def predict(dataset, theta_list):
    x = dataset[:, :-1]
    per_theta_list = [i[0] for i in theta_list]
    per_theta_list = np.array(per_theta_list)
    per_prob = sigmoid(np.dot(x, per_theta_list.T))
    return np.argmax(per_prob, axis=1) # 返回每行最大值所在的索引，即概率最大的类别

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为黑体
    plt.rcParams['axes.unicode_minus'] = False  # 显示负号

    data, target = get_data()
    train, test = split_data(data, target)
    draw_sigmoid()

    iters = 1000 # 迭代次数
    alpha = 0.5 # 学习率
    theta_list = []
    for i in range(data.shape[1]):
        theta = np.zeros((1, data.shape[1]))
        theta_list.append(theta)

    final_theta_list = []
    target_list = list(set(target))

    for i in target_list:
        theta_i = get_final_theta(train, i, theta_list[target_list.index(i)], iters, alpha)
        final_theta_list.append(theta_i)

    y_predict = predict(test, final_theta_list)

    # 输出分类报告
    print(classification_report(y_predict, test[:, -1]))
