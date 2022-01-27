# 同时画正弦函数和抛物线图像

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

# 设置说画图中的中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 准备x, y坐标的数据
x_1 = np.linspace(-10, 10, 1001)  # 生成-10至10之间等距离的1000个数
y_1 = np.sin(x_1)
x_2 = np.linspace(-10, 10, 1001)  # 生成-10至10之间等距离的1000个数
y_2 = x_2 * x_2

# 创建画布
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=80)

# 绘制图像，color、linestyle和label分别设置线条颜色、线型和图例(针对图像层)
axes[0].plot(x_1, y_1, color="r", label="sin()正弦函数", linestyle="-")
axes[1].plot(x_2, y_2, color="b", label="parabola抛物线", linestyle="--")

# 显示图例(针对辅助显示层)
axes[0].legend()
axes[1].legend()

# 准备x的刻度说明
x_label = ["{}".format(int(i)) for i in x_1]
# 修改x, y刻度
axes[0].set_xticks(x_1[::50], x_label[::50])
axes[0].set_yticks(range(-10, 11, 1))
axes[1].set_xticks(x_1[::50], x_label[::50])
axes[1].set_yticks(range(0, 101, 10))

# 添加网格显示
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[1].grid(True, linestyle='--', alpha=0.5)

# 添加x轴描述信息
axes[0].set_xlabel("x轴")
axes[1].set_xlabel("x轴")
# 添加y轴描述信息
axes[0].set_ylabel("y轴")
axes[1].set_ylabel("y轴")
# 添加标题
axes[0].set_title("sin()正弦函数")
axes[1].set_title("parabola抛物线")

# 保存图片
plt.savefig("C:\\Users\\Administrator\\Desktop\\test.jpg")

# 显示图像
plt.show()
