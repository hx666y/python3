
bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000*0.075
bonus3 = bonus2 + 200000*0.05
bonus4 = bonus3 + 200000*0.03
bonus5 = bonus4 + 400000*0.015

def func(num):
    if num <= 100000:
        bonus = num * 0.1
    elif num <= 200000:
        bonus = bonus1 + (num-100000)*0.075
    elif num <= 400000:
        bonus = bonus2 + (num-200000)*0.05
    elif num <= 600000:
        bonus = bonus3 + (num-400000)*0.03
    elif num <= 1000000:
        bonus = bonus4 + (num-600000)*0.015
    else:
        bonus = bonus5 + (num-1000000)*0.01

    return bonus

if __name__ == '__main__':
    print(func(120000))
    print(func(1200000))
    print(func(400000))
    print(func(900000))