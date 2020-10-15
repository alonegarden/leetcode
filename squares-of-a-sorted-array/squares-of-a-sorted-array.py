
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
https://leetcode-cn.com/problems/squares-of-a-sorted-array/
977. 有序数组的平方

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

 
示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

思路： 很简单

"""
def sortedSquares(A) :
  return sorted([a**2 for a in A])

if __name__ == '__main__':
    A = [-4,-1,0,3,10]
    print(sortedSquares(A))

  
"""
class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> vecRet;
        for (int a: A) {
            vecRet.push_back(a * a);
        }
        sort(vecRet.begin(), vecRet.end());
        return vecRet;
    }
};

"""