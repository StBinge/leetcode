#
# @lc app=leetcode.cn id=2289 lang=python3
# @lcpr version=30204
#
# [2289] 使数组按非递减顺序排列
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        temp=[]
        idx=0
        ret=0
        while len(temp) != len(nums):
            ret+=1
            nums=temp
            temp=[]
            N=len(nums)
            idx=0
            while idx<N:   
                j=idx+1
                while j<len(nums) and nums[j]<nums[idx]:
                    j+=1                
                temp.append(nums[idx])
                idx=j
        return ret



# @lc code=end
assert Solution().totalSteps([10,1,2,3,4,5,6,1,2,3]) == 6
assert Solution().totalSteps([4, 5, 7, 7, 13]) == 0
assert Solution().totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]) == 3


#
# @lcpr case=start
# [5,3,4,4,7,3,6,11,8,5,11]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,7,7,13]\n
# @lcpr case=end

#
