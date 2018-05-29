name = input("请输入要复制的文件名:")

f_read = open(name,'r')

findPosition = name.rfind(".")
newName = name[:findPosition] + "[复制]" + name[findPosition:]
f_write = open(newName,'w')

# 开始复制
while True:
    lineContent = f_read.readline()
    if len(lineContent)>0:
        f_write.write(lineContent)
    else:
        break

# 关闭文件
f_read.close()
f_write.close()
