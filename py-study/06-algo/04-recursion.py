
# 1、阶乘运算

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# 2、幂的计算

def power(x,y):
    if y == 1:
        return x
    else:
        return x * power(x, y - 1)

print(power(2,4))

# 3、二分查询

def search(seq, number, lower, upper):
    if lower == upper:
        #assert number != seq[upper]
        print(str(lower))
    else:
        middle = (lower + upper) // 2
        if number > seq[middle]:
            return search(seq, number, middle + 1, upper)
        else:
            return search(seq, number, lower, middle)
search(range(0,100),66,0,100)

