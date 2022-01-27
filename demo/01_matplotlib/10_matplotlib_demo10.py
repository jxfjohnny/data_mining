# 各电影排片占比饼图

from pylab import *
import matplotlib.pyplot as plt

# 设置说画图中的中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']


# 准备二维数据
movie_name = [
    '雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记',
    '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']
place_count = [
    60605, 54546, 45819, 28243, 13270, 9945, 7679, 6799, 6101, 4621, 20105
]

# 创建画布
plt.figure(figsize=(20, 8), dpi=80)

# 绘制图像。autopct参数控制格式
plt.pie(
    place_count, labels=movie_name, autopct="%1.2f%%",
    colors=['b', 'r', 'g', 'y', 'c', 'm', 'b', 'r', 'c', 'g', 'y']
)

# 为了让显示的饼图保持圆形，添加axis保证长宽一致
plt.axis('equal')

# 显示图例
plt.legend(loc="best")

# 添加标题
plt.title("各电影排片占比饼图")

# 保存图片
plt.savefig("C:\\Users\\Administrator\\Desktop\\test.jpg")

# 显示图像
plt.show()
