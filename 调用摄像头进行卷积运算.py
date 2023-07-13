import cv2
import numpy as np

# 定义卷积核
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# 创建VideoCapture对象
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    # 如果帧读取成功，则进行处理
    if ret:
        # 对帧进行卷积操作
        conv_frame = cv2.filter2D(frame, -1, kernel)

        # 增加卷积后图像的亮度和对比度
        alpha = 1.5  # 亮度缩放因子
        beta = 30  # 亮度偏移值
        conv_frame = cv2.convertScaleAbs(conv_frame, alpha=alpha, beta=beta)

        # 在窗口中显示原始帧和卷积后的帧
        cv2.imshow("Original", frame)
        cv2.imshow("Convolution", conv_frame)

        # 按下 q 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # 读取帧失败，退出循环
        break

# 释放摄像头资源
cap.release()

# 关闭所有窗口
cv2.destroyAllWindows()
