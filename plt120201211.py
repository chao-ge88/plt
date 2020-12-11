import os  # 导入os模块
file_path = 'C:\\Users\\air\\Desktop\\1'  # 给出工作簿所在的文件夹路径
file_list = os.listdir(file_path)  # 列出文件夹下所有文件和子文件夹名称
old_book_name = '销售表'  # 给出工作簿名需要替换的旧关键字
new_book_name = '分部产品销售表'  # 给出工作簿名中要替换为的新关键字
for i in file_list:
    if i.startswith('~$'):   # 判断是否有文件名以'~$'开头的临时文件
        continue  # 如果有，则跳过这种类型的文件
    new_file = i.replace(old_book_name, new_book_name)  # 执行查找和替换，生成新的工作薄名
    old_file_path = os.path.join(file_path, i)  # 构造需要重命名工作的完整路径
    new_file_path = os.path.join(file_path, new_file)  # 构造重命名后工作簿的完整路径
    os.rename(old_file_path, new_file_path)  # 执行重命名
