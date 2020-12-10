import xlwings as xw  # 导入xlwings模块
app = xw.App(visible=False, add_book=False)  # 启动excel程序
workbook = app.books.open('C:\\Users\\air\\Desktop\\统计表.xlsx')  # 打开工作簿
worksheets = workbook.sheets  # 获取工作簿中的所有工作表
for i in range(len(worksheets))[:5]:  # 遍历获取到的工作表
    worksheets[i].name = worksheets[i].name.replace('销售', '这次修改前五个')  # 重命名工作表
workbook.save('C:\\Users\\air\\Desktop\\统计表1.xlsx')  # 另存重命名后工作表的工作簿
app.quit()  # 退出excel程序
