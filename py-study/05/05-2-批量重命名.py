import os

# 0. 需要重命名的文件夹
needRenameDir = input("输入要批量重命名的文件夹：")
# 1. 获取指定路径下的所有文件名
allFileName = os.listdir("./"+ needRenameDir)
print(allFileName)
# 2. 循环，依次重命名
for name in allFileName:
   os.rename("./"+ needRenameDir+"/"+name, "./"+needRenameDir+"/"+"[洪哥出品]-"+name) 


