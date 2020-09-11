#!/usr/bin/python
# -*- coding: UTF-8 -*-

##
# https://leetcode-cn.com/problems/compress-string-lcci/
# 字符串压缩
##

"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。
你可以假设字符串中只包含大小写英文字母（a至z）。


思路小结：


"""

from collections import defaultdict


def compressString(S):
    count = 1
    res = ''
    S += ' ' # 边界处理
    for index, val  in enumerate(S[:-1]):
        if val == S[index + 1]: count += 1  
        else: 
            res += val + str(count)
            count = 1
    return res if len(res) < len(S)-1 else S[:-1]


def compressString2(S) :
        count = 1
        res = ''
        slen = len(S)
        for index, val  in enumerate(S):
            if index < len(S)-1 and val == S[index + 1]: count += 1  
            else: 
                res += val + str(count)
                count = 1
        return res if len(res) < len(S) else S

"""
def compressString(S):
    return min( S, "".join(k + str(len(list(v))) for k, v in itertools.groupby(S)), key=len)
"""

if __name__ == '__main__':
	print(compressString("aabcccccaaa")) ## a2b1c5a3
	print (compressString2("abbccd")) # abbccd "abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
	


