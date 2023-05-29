import numpy as np
x_init = np.array([0, 0]) # 初始点
learning_rate = 0.01 # 学习率
num_iterations = 2000 # 迭代次数
epsilon = 1e-11 # 阈值

# 定义目标函数
def f(x1, x2):
    return np.exp(x1 + 3*x2 - 0.1) + np.exp(x1 - 3*x2 - 0.1) + np.exp(-x1 - 0.1)

# 定义目标函数的梯度
def gradient_f(x1, x2):
    df_dx1 = np.exp(x1 + 3*x2 - 0.1) + np.exp(x1 - 3*x2 - 0.1) - np.exp(-x1 - 0.1)
    df_dx2 = 3*np.exp(x1 + 3*x2 - 0.1) - 3*np.exp(x1 - 3*x2 - 0.1)
    return np.array([df_dx1, df_dx2])

# 梯度下降法求解
def gradient_descent(x_init, learning_rate, num_iterations, epsilon):
    x = x_init
    for i in range(num_iterations):
        gradient = gradient_f(x[0], x[1])
        x_next = x - learning_rate * gradient
        if np.linalg.norm(x_next - x) < epsilon:
            break
        x = x_next
    return x, f(x[0], x[1])



# 使用梯度下降法求解
x_star, f_star = gradient_descent(x_init, learning_rate, num_iterations, epsilon)

# 输出结果
print("Minimum value f* = {:.10f}".format(f_star))
print("Optimal point (x1*, x2*) = ({:.10f}, {:.10f})".format(x_star[0], x_star[1]))
