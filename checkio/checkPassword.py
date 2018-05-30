import re

# 方法一
# def checkio(data):
#     r1 = re.match("\w{10}",data)
#     r2 = re.search("[0-9]+",data)
#     r3 = re.search("[a-z]+",data)
#     r4 = re.search("[A-Z]+",data)
#     if bool(r1) and bool(r2) and bool(r3) and bool(r4):
#         return True
#     else:
#         return False

# 方法二
# def checkio(data):
#     if len(data) > 9:
#         if any(i.isupper() for i in data) and any(i.islower() for i in data) and any(i.isdigit() for i in data):
#             return True
#         else:
#             return False
#     else:
#         return False

# 方法三
checkio = lambda data: not(
    len(data) < 10
    or data.isdigit()
    or data.isalpha()
    or data.islower()
    or data.isupper()
)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False
    assert checkio('bAse730onE4') == True
    assert checkio('asasasasasasasaas') == False
    assert checkio('QWERTYqwerty') == False
    assert checkio('123456123456') == False
    assert checkio('QwErTy911poqqqq') == True
    print("check finished.")