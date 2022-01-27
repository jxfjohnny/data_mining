# 电影票房收入绘制例1：对比每部电影的票房收入

from pylab import *
import matplotlib.pyplot as plt

# 设置说画图中的中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 准备x, y坐标的数据
movies_names = [
    '雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记',
    '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它'
]
tickets = [
    73853, 57767, 22354, 15969, 14839, 8725, 8716, 8318, 7916, 6764, 52222
]

# 创建画布
plt.figure(figsize=(20, 8), dpi=80)

# 准备x的刻度说明
x_ticks = range(len(movies_names))
# 绘制图像
plt.bar(x_ticks, tickets,
        color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'b'])

# 添加网格显示
plt.grid(True, linestyle='--', alpha=0.5)

# 修改x的刻度
plt.xticks(x_ticks, movies_names)

# 添加x轴描述信息
plt.xlabel("x轴")
# 添加y轴描述信息
plt.ylabel("y轴")
# 添加标题
plt.title("电影票房收入柱状图")

# 保存图片
plt.savefig("C:\\Users\\Administrator\\Desktop\\test.jpg")

# 显示图像
plt.show()
