# 画出某城市11点到12点1小时内每分钟的温度变化折线图，温度范围在15度-18度，即需要60个(x, y)对

from pylab import *
import random
import matplotlib.pyplot as plt

# 设置说画图中的中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 准备x, y坐标的数据
# 使用`import random`导入random模块，用于生成随机数，uniform使其能够均匀分布
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]

# 创建画布
plt.figure(figsize=(20, 8), dpi=80)

# 绘制图像
plt.plot(x, y_shanghai)

# 准备x的刻度说明
x_label = ["11\'{}\"".format(i) for i in x]
# 修改x, y刻度
plt.xticks(x[::5], x_label[::5])  # x与x_label要一一对应，设置时x及其标签均为每5个单位显示1次
plt.yticks(range(0, 40, 5))  # 设置y的范围是(0, 40)，每5个单位显示1次

# 添加网格显示
plt.grid(True, linestyle='--', alpha=0.5)

# 5.添加x, y轴描述信息及标题等

# 添加x轴描述信息
plt.xlabel("时间")
# 添加y轴描述信息
plt.ylabel("温度")
# 添加标题
plt.title("XX城市的temperature Change status from 11\' to 12\'")

# 保存图片
plt.savefig("C:\\Users\\Administrator\\Desktop\\test.jpg")

# 显示图像
plt.show()
