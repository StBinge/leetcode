#
# @lc app=leetcode.cn id=2869 lang=python3
# @lcpr version=30204
#
# [2869] 收集元素的最少操作次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>k:
                continue
            s.add(nums[i])
            if len(s)==k:
                return len(nums)-i
            
# @lc code=end



#
# @lcpr case=start
# [3,1,5,4,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,1,5,4,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,5,3,1]\n3\n
# @lcpr case=end

#

