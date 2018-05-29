import os

# 0. 获取需要批量删除的目录和字符串
needRenameDir = input("输入文件所在目录：")
dstr = input("输入需要批量删除的字段：")

# 1. 获取需要重命名的文件
allFileName = os.listdir("./"+needRenameDir)

# 2. 批量删除字段
position = len(dstr)
for name in allFileName:
    if len(name)>position and name[:position] == dstr:
        os.rename("./"+needRenameDir+"/"+name,"./"+needRenameDir+"/"+name[position:])
   

