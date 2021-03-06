#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/problems/re-space-lcci/

面试题 17.13. 恢复空格

哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数


输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。


思路小结：动态规划 (https://leetcode-cn.com/problems/re-space-lcci/solution/python-3dong-tai-gui-hua-by-acw_jpch89-4/)




"""

class Solution:

    def respace(self, dictionary, sentence):

        slen = len(sentence)
        if slen == 0: return 0
        if len(dictionary) == 0 : return slen

        dp = [0] * (slen + 1)
        for i in range(1, slen+1):
            dp[i] = dp[i-1] + 1
            for j in range(i) :
                #print(j, i)
                #print (sentence[j:i])
                if sentence[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]


    def respace2(self, dictionary, sentence):

        slen = len(sentence)

        if slen == 0: return 0
        if len(dictionary) == 0 : return slen

        dp = [0] * (slen + 1)
        for i in range(1, slen+1):
            dp[i] = dp[i-1] + 1
            for dict in dictionary:
                if len(dict) <= i and sentence[i-len(dict):i] == dict:
                    dp[i] = min(dp[i], dp[i-len(dict)])
        return dp[-1]



if __name__ == '__main__':

    s = Solution()
    dictionary =  ["looked","just","like","her","brother"]
    sentence = "jesslookedjustliketimherbrother"

    #print(s.ambiguousCoordinates("(123)"))
    #print(s.ambiguousCoordinates("(00011)"))
    #print(s.ambiguousCoordinates("(0123)"))
    print(s.respace2(dictionary, sentence))



