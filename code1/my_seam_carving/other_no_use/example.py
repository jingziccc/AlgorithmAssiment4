import numpy as np
import matplotlib.pyplot as plt

# 创建一个10x10的随机数值表格
data = np.random.random((10, 10))

# 绘制热力图
plt.imshow(data, cmap='gray', vmin=0.0, vmax=1.0)

# 添加数值标签
for i in range(10):
    for j in range(10):
        plt.text(j, i, '{:.2f}'.format(data[i, j]), ha='center', va='center', color='white' if data[i, j] < 0.5 else 'black')

# 设置坐标轴标签
plt.xlabel('Columns')
plt.ylabel('Rows')

# 添加颜色条
plt.colorbar()

# 显示图形
plt.show()
