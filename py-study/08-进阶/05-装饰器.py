def w1(func):
    def inner():
        print("---正在验证权限---")
        if False:
            func()
        else:
            print("权限不足.")
    return inner

#f1 = w1(f1)

@w1
def f1():
    print("----f1----")

@w1
def f2():
    print("----f2----")

f1()
f2()

#给函数增加新的功能，但不改变原函数的代码，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator)
