
# 方法一
def checkio(game_result):
    # 横向
    for i in game_result:
        if i.find("XXX") != -1:
            return "X"
        if i.find("OOO") != -1:
            return "O"
    # 众向
    for j in range(0,3):
        list = []
        for i in range(0,3):
            list.append(game_result[i][j])
        if list[0] == list[1] == list[2] and list[0] != ".":
            return list[0]

    # 斜向
    list = [game_result[i][i] for i in range(0,3)]
    if list[0] == list[1] == list[2] and list[0] != ".":
        return list[0]
    list = [game_result[i][2-i] for i in range(0,3)]
    if list[0] == list[1] == list[2] and list[0] != ".":
        return list[0]

    return "D"
# 方法二
def checkio1(result):
    rows = result
    cols = []
    a = map("".join,zip(*rows))
    for i in a:
        cols.append(i)
    diags = []
    b = map("".join, zip(*[(r[i],r[2-i]) for i,r in enumerate(rows)]))
    for i in b:
        diags.append(i)

    lines = rows + cols + diags
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio1([
        "O.O",
        "XXX",
        ".OO"]) == "X"
    assert checkio1([
        "OO.",
        "XOX",
        "XOX"]) == "O"
    assert checkio1([
        "OOX",
        "XXO",
        "OXX"]) == "D"
    assert checkio1([
        "O.X",
        "XX.",
        "XOO"]) == "X"
    print("OK")
