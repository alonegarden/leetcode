#!/usr/bin/python
# -*- coding: UTF-8 -*-

##
# https://leetcode-cn.com/problems/break-a-palindrome/
# 1328. 破坏回文串
##

"""

给你一个回文字符串 palindrome ，请你将其中 一个 字符用任意小写英文字母替换，使得结果字符串的字典序最小，且 不是 回文串。

请你返回结果字符串。如果无法做到，则返回一个空串。


思路小结：

1. 破坏回文的方法。 所以要知道什么是回文， 什么字典序，
2. 只检查一半数量的字符；
3. 不是'a'的字符就赋值为'a'，
4. 将最后一个字符赋值为'b'。

不知道这题的意义何在？

"""   
import re 

def breakPalindrome(palindrome):
    l = len(palindrome)
    if l == 1:
        return ''
    for index  in range(l // 2):
        if palindrome[index] != 'a':
            return palindrome[:index] + 'a' + palindrome[index + 1:]
    return palindrome[:-1] + 'b'

if __name__ == '__main__':
	
	print(breakPalindrome("abccba") )
	print(breakPalindrome("a") )


