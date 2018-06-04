def func(fn):
    def func_in(*args,**kwargs):  #采用不定长参数的方式满足所有函数需要参数以及不需要参数的情况
        print("----function-start----")
        fn(*args,**kwargs)
        #这个地方,需要写*以及**,如果不写的话,那么args是元祖,而kwargs是字典
        print("----function-end----")
    return func_in


@func
def test(a,b,c):
    print("----test-a=%d,b=%d,c=%d"%(a,b,c))

@func
def test2(a,b,c,d):
    print("----test-a=%d,b=%d,c=%d,d=%d"%(a,b,c,d))
test(1,2,3)
test2(33,44,55,66)

