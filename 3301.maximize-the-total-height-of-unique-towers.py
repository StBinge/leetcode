#
# @lc app=leetcode.cn id=3301 lang=python3
# @lcpr version=30204
#
# [3301] 高度互不相同的最大塔高和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        for i in range(1,len(maximumHeight)):
            maximumHeight[i]=min(maximumHeight[i],maximumHeight[i-1]-1)
            if maximumHeight[i]<1:
                return -1
        return sum(maximumHeight)
# @lc code=end
assert Solution().maximumTotalSum([2,3,4,3])==10


#
# @lcpr case=start
# [2,3,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [15,10]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

#

