def makeBold(fn):
    def wrapped():
        print("----1----")
        return "<b>"+fn()+"</b>"
    return wrapped

def makeItalic(fn):
    def wrapped():
        print("----2----")
        return "<i>"+fn()+"</i>"
    return wrapped

@makeBold
@makeItalic
def test():
    print("----base----")
    return "hello world"

ret = test()
print(ret)
