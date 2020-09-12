#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/problems/ambiguous-coordinates/

816. 模糊坐标

我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。

原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。

最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。


思路小结：（网友解题思路）

1. 先将输入拆成两步份，分别得到一组数，然后计算笛卡尔积就是结果
2. 对于拆出来的数字 主要有两个个判断，然后枚举小数点位置即可
3. 如果第一个字符为0 那么 要么这个数字是 0 要么这个数字是 0.xxx
4. 如果结尾是0 那么这个数不能是是小数


"""   

class Solution:

    def get_number(self, s: str):
        
        if s != '0' and s[0] == '0': #  第一个是0的情况：  001 0000
            return ["0." + s[1:]] if s[-1] != '0' else []
        if s[-1] == '0':
            return [s]
        number = [s]
        for i in range(1, len(s)):
            number.append(s[:i] + "." + s[i:])
        return number

    def ambiguousCoordinates(self, s:str):
        ret = []
        s = s[1:-1]
        for i in range(1, len(s)):
            x = self.get_number(s[:i])
            y = self.get_number(s[i:])
            #print(s[:i], x)
            #print(s[i:], y)
            for i in x:
                for j in y:
                    ret.append("(%s, %s)" % (i,j))
        return ret

   

if __name__ == '__main__':

    s = Solution()
    #print(s.ambiguousCoordinates("(123)"))
    #print(s.ambiguousCoordinates("(00011)"))
    #print(s.ambiguousCoordinates("(0123)"))
    print(s.ambiguousCoordinates("(1100)" ))
    


