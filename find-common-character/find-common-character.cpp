
/*
https://leetcode-cn.com/problems/find-common-characters/submissions/

1002. 查找常用字符

给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

 
示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]


*/

class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        vector<string> result;
        if (A.size() == 0) return result;
        int T[26] = {0}; // 26个字母

        /// 统计第一个字符
        for (int i = 0; i < A[0].size(); i++) { 
            T[A[0][i] - 'a']++;
        }
        
        /// 统计其他的字符
        int TOtherStr[26] = {0}; // 统计除第一个字符串外字符的出现频率
        for (int i = 1; i < A.size(); i++) {
            memset(TOtherStr, 0, 26 * sizeof(int));
            for (int j = 0; j < A[i].size(); j++) {
                TOtherStr[A[i][j] - 'a']++;
            }
            /// 取出小的那个，如果是0，则说明，有字符串没有出现这个字母 
            for (int k = 0; k < 26; k++) { 
                T[k] = min(T[k], TOtherStr[k]);
            }
        }
        
        /// 输出
        for (int i = 0; i < 26; i++) {
            while (T[i] != 0) { 
                string s(1, i + 'a'); 
                result.push_back(s);
                T[i]--;
            }
        }

        return result;
    }
};