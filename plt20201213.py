import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.open('C:\\Users\\air\\Desktop\\20201213\\1.xlsx')
sheet = workbook.sheets[0]
info = sheet.used_range
for i in info.raw_value[1:]:
    print(i)
    app = xw.App(visible=True, add_book=False)
    workbook = app.books.open('C:\\Users\\air\\Desktop\\20201213\\2.xlsx')
    sheet = workbook.sheets[0]
    sheet['B1'].value = i[0]
    sheet['D1'].value = i[1]
    sheet['F1'].value = i[8]
    sheet['H1'].value = i[2]
    sheet['B2'].value = i[9]
    sheet['D2'].value = i[5]
    sheet['F2'].value = i[6]
    sheet['H2'].value = i[7]
    workbook.save('C:\\Users\\air\\Desktop\\20201213\\{}.xlsx'.format(i[0]))
    workbook.close()
    app.quit()
