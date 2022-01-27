# 多个坐标系显示--plt.subplots(面向对象的画图方法)
# 从创建画布开始，将面向过程的编程修改为面向对象的编程

from pylab import *
import random
import matplotlib.pyplot as plt

# 设置说画图中的中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 准备x, y坐标的数据
# 使用`import random`导入random模块，用于生成随机数，uniform使其能够均匀分布
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 3) for i in x]

# 创建画布
# plt.figure(figsize=(20, 8), dpi=80)
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=80)

# 绘制图像，color和linestyle分别设置线条颜色和线型(针对图像层)
axes[0].plot(x, y_shanghai, color="r", label="Shanghai", linestyle="--")
axes[1].plot(x, y_beijing, color="b", label="Beijing")

# 显示图例(针对辅助显示层)
axes[0].legend()
axes[1].legend()

# 准备x的刻度说明
x_label = ["11\'{}\"".format(i) for i in x]
# 修改x, y刻度
axes[0].set_xticks(x[::5], x_label[::5])
axes[0].set_yticks(range(0, 40, 5))
axes[1].set_xticks(x[::5], x_label[::5])
axes[1].set_yticks(range(0, 40, 5))


# 添加网格显示
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[1].grid(True, linestyle='--', alpha=0.5)

# 5.添加x, y轴描述信息及标题等

# 添加x轴描述信息
axes[0].set_xlabel("时间")
axes[1].set_xlabel("时间")
# 添加y轴描述信息
axes[0].set_ylabel("温度")
axes[1].set_ylabel("温度")
# 添加标题
axes[0].set_title("XX城市的temperature Change status from 11\' to 12\'")
axes[1].set_title("XX城市的temperature Change status from 11\' to 12\'")

# 保存图片
plt.savefig("C:\\Users\\Administrator\\Desktop\\test.jpg")

# 显示图像
plt.show()
