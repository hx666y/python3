
def checkio(data):
    newList = []
    for i in data:
        if data.count(i)>1:
            newList.append(i)
    return newList

def checkio1(data):
    return [x for x in data if data.count(x)>1]

if __name__ == '__main__':
    assert checkio([1,1,2,3,4,4]) == [1,1,4,4]
    assert checkio1([4,5,6,7,4,3,2,2]) == [4,4,2,2]
    print("OK")