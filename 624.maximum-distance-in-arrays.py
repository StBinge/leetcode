#
# @lc app=leetcode.cn id=624 lang=python3
# @lcpr version=30204
#
# [624] 数组列表中的最大距离
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi=float('inf')
        mx=float('-inf')
        ret=0
        for ar in arrays:
            ret=max(ret,mx-ar[0],ar[-1]-mi)
            mi=min(mi,ar[0])
            mx=max(mx,ar[-1])
        return ret


# @lc code=end
assert Solution().maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]) == 14
assert Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) == 4
assert Solution().maxDistance([[1], [1]]) == 0


#
# @lcpr case=start
# [[1,2,3],[4,5],[1,2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[1]]\n
# @lcpr case=end

#
