#
# @lc app=leetcode.cn id=2848 lang=python3
# @lcpr version=30204
#
# [2848] 与车相交的点
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()

        end=0
        ret=0
        for x,y in nums:
            if end<y:
                ret+=y-max(end,x-1)
                end=y
        return ret
# @lc code=end
assert Solution().numberOfPoints([[3,6],[1,5],[4,7]])==7


#
# @lcpr case=start
# [[3,6],[1,5],[4,7]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,8]]\n
# @lcpr case=end

#

