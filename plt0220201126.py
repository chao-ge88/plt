import matplotlib.pyplot as plt
#  解决图中不显示中文的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=4)
#  设置图表标题并给坐标轴加标签
ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)
#  设置刻度标记的大小，并影响x轴与y轴。
ax.tick_params(axis='both', labelsize=14)

plt.show()