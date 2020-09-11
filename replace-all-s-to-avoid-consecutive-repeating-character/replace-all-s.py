#!/usr/bin/python
# -*- coding: UTF-8 -*-

##
# https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
# 		
##

"""
给你一个仅包含小写英文字母和 '?' 字符的字符串 s<var> </var>，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。

注意：你 不能 修改非 '?' 字符。

题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。

在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。

思路小结：
1. 处理一下原数据，前后加0（只要小写字母就可以）
2. 预备要处理的字母，
3. 两次循环，第一次判断是否是`?`,第二次找出可以替换字母判断前后是否一样。
4. 注意要先处理成list
    
"""

def modifyString(s):

	magic = "abcdefghijklmnopqrstuvwxyz"
	s = "0" + s + "0"
	lists = list(s)
	for index, byte  in enumerate(lists): 
		if byte == '?' : 
			for m in magic:
				if m != lists[index-1] and m !=lists[index+1]:
					lists[index] = m
	return  ''.join(lists[1:-1])

if __name__ == '__main__':
	print (modifyString("ubv?w"))

	print (modifyString("j?qg??b"))

	print (modifyString("??yw?ipkj?"))

