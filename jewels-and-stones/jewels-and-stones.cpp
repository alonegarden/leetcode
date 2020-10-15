
/*
https://leetcode-cn.com/problems/jewels-and-stones/

771. 宝石与石头

给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

示例 1:

输入: J = "aA", S = "aAAbbbb"
输出: 3

思路： 

  1 把S写入set中
  2 如果Set已经存在则加1
  
*/

class Solution {
public:
    int numJewelsInStones(string J, string S) {

        if (J.empty() || S.empty())  return 0; 
        std::set<char> setTmp; 
        for (size_t i=0; i<J.length();++i){
            setTmp.insert(J[i]);
        }
        int ret = 0; 
        for (size_t i=0; i<S.length();++i){
            ret += setTmp.count(S[i]);
        }
        return ret; 
    }
};