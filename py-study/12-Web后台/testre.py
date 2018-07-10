import re

pattern = re.compile('/({[^{}:]+:?[^{}:]*})')
s = '/student/{name:str}/xxx/{id:int}'
s1 = '/student/xxx/{id:int}/yyy'
s2 = '/student/xxx/5134324'
s3 = '/student/{name:}/xxx/{id}'
s4 = '/student/{name:}/xxx/{id:aaa}'

TYPEPATTERNS = {
    'str': r'[^/]+',
    'word': r'\w+',
    'int': r'[+-]?\d+',
    'float': r'[+-]?\d+\.\d+',
    'any': r'.+'
}

TYPECAST = {
    'str': str,
    'word': str,
    'int': int,
    'float': float,
    'any': str
}

def transform(kv: str):
    # /{id:int} => /(?P<id>[+-]?\d+)
    name, _, type = kv.strip('/{}').partition(':')
    # 返回元组， (目标正则表达式， 被替换部分类型有序列表)
    return '/(?P<{}>{})'.format(name, TYPEPATTERNS.get(type, '\w+')), name, TYPECAST.get(type, str)

def parse(src: str):
    start = 0
    res = ''
    translator = {}
    while True:
        matcher = pattern.search(src, start)
        if matcher:
            # print(matcher.group())
            res += matcher.string[start:matcher.start()]
            tmp = transform(matcher.string[matcher.start():matcher.end()])
            res += tmp[0]
            translator[tmp[1]] = tmp[2]
            start = matcher.end()
        else:
            break
    # 没有任何匹配应该原样返回字符串
    if res:
        return res, translator
    else:
        return res, translator

print(parse(s))
print(parse(s1))
print(parse(s2))
print(parse(s3))
print(parse(s4))