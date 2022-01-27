# 电影票房收入绘制例2：对比不同电影首日和首周的票房

from pylab import *
import matplotlib.pyplot as plt

# 设置说画图中的中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 准备x, y坐标的数据
movies_names = ['雷神3：诸神黄昏', '正义联盟', '寻梦环游记']
first_day = [10587.6, 10062.5, 1275.7]
first_week = [36224.9, 34479.6, 11830]

# 创建画布
plt.figure(figsize=(20, 8), dpi=80)

# 准备x的刻度说明
x_ticks = range(len(movies_names))
# 绘制图像
plt.bar(x_ticks, first_day, width=0.2, label="首日票房")
# 括号中[i + 0.2 for i in x_ticks]，用的是列表生成式
plt.bar([i + 0.2 for i in x_ticks], first_week, width=0.2, label="首周票房")

# 显示图例
plt.legend()

# 添加网格显示
plt.grid(True, linestyle='--', alpha=0.5)

# 修改x的刻度
plt.xticks([i + 0.1 for i in x_ticks], movies_names)

# 添加x轴描述信息
plt.xlabel("x轴")
# 添加y轴描述信息
plt.ylabel("y轴")
# 添加标题
plt.title("各电影首日/首周票房柱状图")

# 保存图片
plt.savefig("C:\\Users\\Administrator\\Desktop\\test.jpg")

# 显示图像
plt.show()
