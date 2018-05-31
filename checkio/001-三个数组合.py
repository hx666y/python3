
# 1,2,3,4  组成不重复的三位数

def func():
    list = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if (i != j) and (i != k) and (j != k):
                    list.append(i*100 + j*10 + k)

    return list

if __name__ == '__main__':
    print(func())