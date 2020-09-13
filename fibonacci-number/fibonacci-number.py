#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
# https://leetcode-cn.com/problems/fibonacci-number/
# 509. 斐波那契数
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 
思路小结：

0. 可以算是动态规划算法的题
1. 很简单的题，存在前面两个数的值，算出第三个，
2. 注意 0 1 2 的值。
3. 如果用递归时间比较大， O(2^n) 次
"""

class Solution:

    def fib(self, N: int):
        if N == 0 : return 0
        if N == 2 or N == 1: return 1
        prev = 1
        curr = 1
        for i in range(3, N+1):
            #print (i)
            sum = prev + curr
            prev = curr
            curr = sum
        return curr


if __name__ == '__main__':

    s = Solution()
    print(s.fib(2))
    print(s.fib(3))
    print(s.fib(4))


