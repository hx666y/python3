import string

def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

# def checkio(text):
#     # 先转换成小写然后倒序
#     text = "".join((lambda x: (x.sort(), x)[1])(list(text.lower())))
#     dict = {}
#     for str in text:
#         if str.isalpha():
#             if str in dict:
#                 dict[str] += 1
#             else:
#                 dict[str] = 1
#
#     return max(dict, key=dict.get)


if __name__ == '__main__':
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo!!!!") == "a"
    assert checkio("abe") == "a"
    assert checkio("a" * 9000 + "b" * 1000) == "a"
    print("The local tests are done.")