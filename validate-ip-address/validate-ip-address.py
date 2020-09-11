#!/usr/bin/python
# -*- coding: UTF-8 -*-

##
# https://leetcode-cn.com/problems/validate-ip-address/
# 验证IP地址
##

"""
编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。

IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；

同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。

同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。



思路小结：
1. 这题没什么算法可言， 按字符串特征分解，判断合法性
2. ipv4  '.' 分成4个数字， 大于0 小于255，第一个不能为0 
3.ipv5  ':' 分成8个数字（十六进制） 每部分合法判断

"""

from collections import defaultdict


def validIPAddress(IP):
    if '.' in IP:
        lists = IP.split('.')
        if len(lists) != 4: return 'Neither'
        print (lists)
        for num in lists:
            if len(num) == 0 or len(num) > 3: return 'Neither'
            if not num.isdigit(): return  'Neither'
            if int(num[0]) == 0 and len(num) > 1: return 'Neither'
            if int(num) > 255: return 'Neither'
        return 'IPv4'
    elif ':' in IP: 
        lists = IP.split(':')
        if len(lists) != 8:  return 'Neither'
        hexnum = '1234567890abcdefABCDEF'
        for num in lists: 
            if len(num) == 0 or len(num) > 4 : return 'Neither'
            #if [False for n in num if n not in hexnum]: return 'Neither'
            for n in num:   
                if  n not in hexnum: return  'Neither'
        return 'IPv6'
    return 'Neither'
        


if __name__ == '__main__':
    print(validIPAddress("A.a.aA.2")) 
    print(validIPAddress("1e1.4.5.6"))  
    print(validIPAddress("20EE:Fb8:85a3:0:0:8A2E:0370:7334:12")) 
    #print(validIPAddress("256.256.256.256")) 
	


