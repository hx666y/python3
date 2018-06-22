from multiprocessing import Pool,Manager
import os

def copyFileTask(name, oldFolderName, newFolderName,queue):
    #print(name)
    fr = open(oldFolderName + "/" + name)
    fw = open(newFolderName + "/" + name, "w")
    #print("---------")
    content = fr.read()
    fw.write(content)
    queue.put(name)

    fr.close()
    fw.close()

def main():
    #0 获取要copy的文件夹的名字
    oldFolderName = input("请输入文件夹的名字:")

    #1 创建一个文件夹
    newFolderName = oldFolderName + "-复件"
    #print(newFolderName)
    os.mkdir(newFolderName)

    #2 获取old文件夹中的所有文件名字
    filenames = os.listdir(oldFolderName)
    #print(filenames)
    
    #3 使用多进程的方式copy
    pool = Pool(5)
    queue = Manager().Queue()

    for name in filenames:
        pool.apply_async(copyFileTask, args=(name,oldFolderName,newFolderName,queue))

    num = 0
    allNum = len(filenames)
    while num<allNum:
        queue.get()
        num += 1
        copyRate = num/allNum
        print("\rcopy的进度是:%.2f%%"%(copyRate*100),end="")
        
    #pool.close()
    #pool.join()
    print("\nCopy Finished...Total num is %d"% num)


if __name__ == "__main__":
    main()
