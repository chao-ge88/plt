import xlwings as xw
import pandas as pd
app = xw.App(visible=False)
workbook = app.books.add()
worksheet = workbook.sheets.add('pandas&xlwings实践表')
df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['a', 'b'])
worksheet.range('A1').value = df
workbook.save(r'C:\Users\air\Desktop\table.xlsx')
workbook.close()
app.quit()
