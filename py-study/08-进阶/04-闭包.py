def test(a,b):
    def test_in(x):
        print(a*x+b)
    return test_in

line = test(10,4)
line(1)
