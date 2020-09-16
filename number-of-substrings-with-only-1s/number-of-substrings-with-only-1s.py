#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
# https://leetcode-cn.com/problems/number-of-substrings-with-only-1s/
# 1249. 移除无效的括号

给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。

返回所有字符都为 1 的子字符串的数目。

由于答案可能很大，请你将它对 10^9 + 7 取模后返回。

输入：s = "0110111"
输出：9
解释：共有 9 个子字符串仅由 '1' 组成
"1" -> 5 次
"11" -> 3 次
"111" -> 1 次


思路小结：

1. 按0 分割出只有1的子串
2. 长度为n的连续的1可以构成 n * (n + 1) / 2 子串，求所有子串的总和
"""
import re

def numSub(s):
   return sum([len(i) * (len(i) + 1) // 2 for i in s.split('0')]) % (1000000007)

if __name__ == '__main__':

    print(numSub("0110111"))
    print(numSub("101"))



