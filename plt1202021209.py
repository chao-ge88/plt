import xlwings as xw
app = xw.App(visible=True, add_book=False)  # 启动excel程序，但不新建工作簿
for i in range(20):
    workbook = app.books.add()  # 新建工作簿
    workbook.save(f'C:\\Users\\air\\Desktop\\1\\test{i}.xlsx')  # 保存新建的多个工作簿
    workbook.close()  # 关闭当前工作簿
app.quit()  # 退出excel程序
