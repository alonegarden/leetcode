
/*
https://leetcode-cn.com/problems/two-sum/

1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]


思路： 

  1 把S写入set中
  2 如果Set已经存在则加1
  
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> mapTmp; 
        for (int i=0; i<nums.size(); ++i){
            int other = target - nums[i];
            auto it = mapTmp.find(other); 
            if (it != mapTmp.end()) {
                return {it->second, i};
            }
            mapTmp[nums[i]] = i;
        }
        return {};
    }

    
};