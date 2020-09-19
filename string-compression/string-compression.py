#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
# https://leetcode-cn.com/problems/string-compression/
# 443. 压缩字符串

给定一组字符，使用原地算法将其压缩。

压缩后的长度必须始终小于或等于原数组长度。

数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。

在完成原地修改输入数组后，返回数组的新长度。


进阶：
你能否仅使用O(1) 空间解决问题？


示例 1：

输入：
["a","a","b","b","c","c","c"]

输出：
返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]

说明：
"aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。


思路小结：

1. 原地算法: 一句话总结就是: 原地算法不依赖额外的资源或者依赖少数的额外资源，仅依靠输出来覆盖输入的一种算法操作。
2. 边界用空格，不会对字符串产生污染。
3. 用pos标示压缩后字符串最后位置， 即pos为压缩后字符串的长度
4. 当有字符相同时，count 用做计数，记得重新开始要记为 1
5. 依次比较前后两个字符，
6. 如果相等，则用count累计
7. 如果不等，则把最后一个字段写入pos位置，然后pos后移。
8. 然后把累计数字转成字符串加在后面。
9. 如果count=1, 则不用处理。
10. count!=1, 则把数据加在pos位置后面，同pos后移
11. 最后pos指向的位置的大小就是压缩后的长度。pos前面的字符串，不是压缩后的字符串。

"""

def compress(chars):
    if len(chars) == 1: return len(chars)
    chars.append(' ')
    count, pos = 1, 0
    for i in range(1,len(chars)):
        if chars[i] != chars[i-1]:
            chars[pos] = chars[i-1]
            pos += 1

            if count > 1:
                for j in range(len(str(count))):
                    chars[pos + j] = str(count)[j]
                pos += len(str(count))
            count = 1
        else:
            count += 1

    return pos


if __name__ == '__main__':

    chars = ["a","a","b","b","c","c","c"]
    print(compress(chars))

    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(compress(chars))




