import os
file_path = 'C:\\Users\\air\\Desktop\\1'  # 给出工作簿所在的文件夹路径
file_list = os.listdir(file_path)  # 列出路径下所有文件和子文件夹的名字
for i in file_list:
    print(i)