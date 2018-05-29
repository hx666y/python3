aStr = "hello world ,hhhh world heihei"

def replaceStr(string, oldStr, newStr):
    while True:
        #print(string)
        position = string.find(oldStr)
        if position == -1:
            break
        string = string[:position] + newStr + string[position+len(oldStr):]
    return string

def replaceStr2(temp, oldStr, newStr):
    result = temp.split(oldStr)
    return newStr.join(result)

result = replaceStr2(aStr,"h","H")
print(result)
