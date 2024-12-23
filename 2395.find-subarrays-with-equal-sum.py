#
# @lc app=leetcode.cn id=2395 lang=python3
# @lcpr version=30204
#
# [2395] 和相等的子数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen=set()
        for x,y in pairwise(nums):
            s=x+y
            if s in seen:
                return True
            seen.add(s)
        return False
        
# @lc code=end



#
# @lcpr case=start
# [4,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

