import os  # 导入os模块
import xlwings as xw  # 导入xlwings模板
file_path = 'C:\\Users\\air\\Desktop\\1'  # 给出工作簿所在的文件夹路径
file_list = os.listdir(file_path)  # 列出路径下所有文件和子文件夹的名字
app = xw.App(visible=True, add_book=False)  # 启动excel程序
for i in file_list:
    if os.path.splitext(i)[1] == '.xlsx':  # 判断文件夹下文件的扩展名是否为“.xlsx”
        app.books.open(file_path + '\\' + i)  # 打开工作簿
