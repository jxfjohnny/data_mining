# 电影时长频数分布直方图

from pylab import *
import matplotlib.pyplot as plt

# 设置说画图中的中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 准备x, y坐标的数据
time = [
    141, 132, 86, 110, 116, 148, 99, 84, 50, 165, 104, 89, 100, 111, 128,
    108, 85, 56, 34, 137, 80, 124, 147, 126, 71, 68, 42, 190, 144, 91, 139,
    134, 103, 70, 51, 164, 162, 114, 156, 142, 140, 83, 95, 127, 179, 101,
    112, 131, 177, 65, 123, 113, 133, 167, 47, 72, 117, 96, 87, 94, 102, 81,
    73, 107, 90, 82, 58
]

# 创建画布
plt.figure(figsize=(20, 8), dpi=80)

# 设置组距/组数
distance = 4
group_num = int((max(time) - min(time)) / distance)
# 绘制图像。添加上density=True的参数后y轴显示频率，否则显示频数
plt.hist(time, bins=group_num, density=True)
# plt.hist(time, bins=group_num)

# 修改x的刻度
plt.xticks(range(min(time), max(time) + 1)[::distance])

# 添加网格显示
plt.grid(True, linestyle='--', alpha=0.5)

# 添加x轴描述信息
plt.xlabel("x轴：电影时长区间")
# 添加y轴描述信息
plt.ylabel("y轴：电影数据量")
# 添加标题
plt.title("电影时长频数分布直方图")

# 保存图片
plt.savefig("C:\\Users\\Administrator\\Desktop\\test.jpg")

# 显示图像
plt.show()
