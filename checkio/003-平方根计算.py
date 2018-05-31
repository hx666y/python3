import math

def func():
    list = []
    for i in range(10000):

        x = int(math.sqrt(i+100))
        y = int(math.sqrt(i+268))

        if (x*x==(i+100)) and (y*y==(i+268)):
            list.append(i)
    return list

if __name__ == '__main__':
    print(func())
