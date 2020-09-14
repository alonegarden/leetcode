#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
# https://leetcode-cn.com/problems/coin-change/
# 322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

输入: coins = [2], amount = 3
输出: -1

思路小结：

0. 动态规划算法题


"""

import re

class Solution:

   def coinChange(self, coins, amount ):
        f = [float('inf')]*(amount+1)
        f[0] = 0
        for c in coins:  # 枚举硬币种数
            for j in range(c, amount+1):  # 从小到大枚举金额，确保j-c >= 0.
                    f[j] = min(f[j], f[j - c] + 1)
        return f[amount] if f[amount] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。


if __name__ == '__main__':

    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(s.coinChange(coins, amount))



