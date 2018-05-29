# 列表保存所有学生的所有信息
stuInfos = []

# 打印功能提示
def printMenu():
    print("="*30)
    print("      学生管理系统V1.0")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 保存数据")
    print("0. 退出系统")
    print("="*30)

def getInfo():
    newName = input("请输入新学生的名字：")
    newSex = input("请输入新学生的性别：(男/女)")
    newPhone = input("请输入新学生的手机号码：")
    return {'name':newName,'sex':newSex,'phone':newPhone}

def addStuInfo():
    result = getInfo()
    newInfo = {}
    newInfo['name'] = result['name']
    newInfo['sex'] = result['sex']
    newInfo['phone'] = result['phone']
    stuInfos.append(newInfo)

def modifyStuInfo():
    stuId = input("请输入要修改的学生的序号：")
    stuId = int(stuId)
    result = getInfo()
    stuInfos[stuId-1]['name'] = result['name']
    stuInfos[stuId-1]['sex'] = result['sex']
    stuInfos[stuId-1]['phone'] = result['phone']

def save2file():
    f = open("backup.data", "w")
    f.write(str(stuInfos))
    f.close()

def recoverData():
    global stuInfos
    f = open("backup.data")
    content = f.read()
    stuInfos = eval(content)
    f.close()

def main():
    recoverData()
    while True:
        printMenu()
        key = input("请输入功能对应的数字：")
        if key == "0":
            break
        elif key == "1":
            #添加学生信息
            addStuInfo()
        elif key == "3":
            modifyStuInfo()
        elif key == "5":
            #print(stuInfos)
            print("="*30)
            print("学生信息如下:")
            print("="*30)
            print("序号\t姓名\t性别\t手机")
            i = 1
            for tempInfo in stuInfos:
                print("%d\t%s\t%s\t%s"%(i,tempInfo['name'], tempInfo['sex'], tempInfo['phone'] ))
                i += 1
        elif key == "6":
            save2file()  
            

main()
