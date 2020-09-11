#!/usr/bin/python
# -*- coding: UTF-8 -*-

##
# https://leetcode-cn.com/problems/calculator-lcci/
# 计算器
##

"""
思路小结：

1. 用栈
2. 第一个数字前面加+
3. 把+和-后面的值加入栈中，如果是*和/就从栈中拿出第一个数字，然后运算后加回去
4. 把栈中的所个数字相加
5. 正则分离数字
"""

import re 

def calculator_lcci(args):
	stack = []
	args ='+'+ args
	patt = re.compile(r'\d+|\+|\*|-|/')
	args = patt.findall(args.replace(' ',''))
	
	for i, arg in enumerate(args):
		if i % 2 != 1:
			continue
		
		if args[i-1] == '+': stack.append(int(arg))
		elif args[i-1] == '-': stack.append(-int(arg))
		else:
			arg2 = stack.pop()
			if args[i-1] =='/': stack.append(int(arg2/int(arg)))
			if args[i-1] == '*':stack.append(arg2*int(arg))
	
	return sum(stack)

if __name__ == '__main__':
	
	print(calculator_lcci("2+6/2") )
	print(calculator_lcci("2+22-6/2") )
	print(calculator_lcci("2+6*2"))


