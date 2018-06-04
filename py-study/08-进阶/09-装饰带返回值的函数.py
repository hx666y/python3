def func(fn):
    def func_in():
        print("----func_in-start----")
        ret = fn()
        return ret
    return func_in

@func 
def test():
    print("----test----")
    return "done"

ret = test()
print(ret)
