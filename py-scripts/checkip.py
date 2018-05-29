#!/usr/bin/python
#coding:utf-8
import re
import sys
import urllib.request

def check_ip(ip):
    # 精确的匹配给定的字符串是否是IP地址
    if re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip):
        return "1"
    else:
        return "0"
    # # 从长文本中提取中提取ip地址
    # string_ip = "is this 255.22.22.26 ip ?"
    # result = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', string_ip)
    # if result:
    #     print(result)
    # else:
    #     print("re cannot find ip")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("输入IP")
        sys.exit()
    ip = sys.argv[1]
    response = check_ip(ip)
    if response == "0":
        print("error.")
    if response == '1':
        print("right.")
       
