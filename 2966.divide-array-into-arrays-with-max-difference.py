#
# @lc app=leetcode.cn id=2966 lang=python3
# @lcpr version=30204
#
# [2966] 划分数组并满足最大差限制
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ret=[]
        for i in range(0,len(nums),3):
            if nums[i+2]-nums[i]<=k:
                ret.append(nums[i:i+3])
            else:
                return []
        return ret
            
# @lc code=end



#
# @lcpr case=start
# [1,3,4,8,7,9,3,5,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,4,2,2,5,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]\n14\n
# @lcpr case=end

#

