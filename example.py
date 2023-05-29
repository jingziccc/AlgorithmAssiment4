import numpy as np
import matplotlib.pyplot as plt

def visualize_quadratic_function(a, b, c, learning_rate=0.1, num_iterations=10):
    # 生成一定范围内的 x 和 y 值
    x = np.linspace(-20, 20, 100)
    y = np.linspace(-20, 20, 100)
    X, Y = np.meshgrid(x, y)
    
    # 计算对应的 z 值
    Z = a * X**2 + b * Y**2 + c
    
    # 创建图形窗口
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制函数图像
    ax.plot_surface(X, Y, Z)
    
    # 设置坐标轴标签
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    # 添加标题
    ax.set_title('Quadratic Function')
    
    # 初始化起始点
    start_x = -9
    start_y = 3
    start_z = a * start_x**2 + b * start_y**2 + c
    
    # 绘制起始点
    ax.scatter(start_x, start_y, start_z, color='yellow')
    
    # 迭代更新点
    for i in range(num_iterations):
        # 计算梯度
        gradient_x = 2 * a * start_x
        gradient_y = 2 * b * start_y
        
        # 根据梯度和学习率更新点
        start_x -= learning_rate * gradient_x
        start_y -= learning_rate * gradient_y
        start_z = a * start_x**2 + b * start_y**2 + c
        
        # 绘制更新后的点
        ax.scatter(start_x, start_y, start_z, color='red')
    
    # 显示图像
    ax.legend()
    plt.show()

# 示例用法
visualize_quadratic_function(2, 1, 3, learning_rate=0.1, num_iterations=10)
