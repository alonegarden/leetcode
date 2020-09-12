#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
# https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses/
# 1249. 移除无效的括号

给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 任意一条 要求：

 * 空字符串或只包含小写字母的字符串
 * 可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
 * 可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」


思路小结：

1. 定义两个栈， 一个左括号，一个或括号
2. 如果是左括号，则用一个栈记录位置， 如果是右括号，则看一下左边的栈有没有记录，有则清掉一个，
3. 没有则位置添加右边栈中
4. 把有位置记录的符号清除掉 

"""   
import re 

def minRemoveToMakeValid(s):
    l_stack = []
    r_stack = []
    for i, b in enumerate(s): 
        if b not in ('(', ')'): continue
        if b == '(': l_stack.append(i)
        if b == ')': 
            if len(l_stack) != 0: l_stack.pop()
            else: r_stack.append(i)
    new_one = ''
    for i in range(len(s)): 
        if i not in l_stack and i not in r_stack:
            new_one += s[i]
    return new_one

if __name__ == '__main__':

    print(minRemoveToMakeValid("lee(t(c)o)de)"))
    print(minRemoveToMakeValid("a)b(c)d"))
    print(minRemoveToMakeValid("))(("))
    print(minRemoveToMakeValid("(a(b(c)d)"))



