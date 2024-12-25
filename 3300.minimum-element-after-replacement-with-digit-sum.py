#
# @lc app=leetcode.cn id=3300 lang=python3
# @lcpr version=30204
#
# [3300] 替换为数位和以后的最小元素
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ret=nums[0]
        for n in nums:
            cur=0
            while n:
                cur+=n%10
                n//=10
            ret=min(cur,ret)
        return ret
# @lc code=end



#
# @lcpr case=start
# [10,12,13,14]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [999,19,199]\n
# @lcpr case=end

#

