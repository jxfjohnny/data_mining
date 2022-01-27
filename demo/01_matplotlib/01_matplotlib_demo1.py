# 展现一周的天气，如：从星期一到星期日的天气温度

import matplotlib.pyplot as plt
# matplotlib inline

# 创建画布
plt.figure(figsize=(20, 8), dpi=80)

# 绘制图像
plt.plot(
    [1, 2, 3, 4, 5, 6, 7],
    [17, 17, 18, 15, 11, 11, 13]
)

# 显示图像
plt.show()
