def func(fn):
    def func_in(*args,**kwargs):
        print("----记录日志----")
        ret = fn(*args,**kwargs)
        return ret
    return func_in

@func
def test():
    return "test"

@func
def test1(a):
    return a

print(test())
print(test1(11))
