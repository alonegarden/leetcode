#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
# https://leetcode-cn.com/problems/single-number/
# 136. 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

思路小结：

1. 用异或的方法

"""

def singleNumber(nums):

    ret = 0
    for n in nums:
        ret ^= n
    return ret


if __name__ == '__main__':

    nums = [2, 2, 1]
    print(singleNumber(nums))



