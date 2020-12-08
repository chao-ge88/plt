import xlwings as xw
import matplotlib.pyplot as plt
figure = plt.figure()
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add('plt&xlwings实践表')
# 将绘制的图表写入工作簿
worksheet.pictures.add(figure, name='图片一', update=True, left=100)
workbook.save(r'C:\Users\air\Desktop\plt和xlwings结合.xlsx')
workbook.close()
app.quit()
