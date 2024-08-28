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
        mx1 = mx2 = float("-inf")
        mx1id = mx2id = -1
        mi1 = mi2 = float("inf")
        mi1id = mi2id = -1
        for i in range(len(arrays)):
            ar = arrays[i]
            mi, mx = ar[0], ar[-1]
            if mi < mi1:
                mi1, mi2 = mi, mi1
                # mi1id,mi2id=i,mi1id
                mi1id = i
            elif mi < mi2:
                mi2 = mi
                # mi2id=i

            if mx > mx1:
                mx1, mx2 = mx, mx1
                # mx1id,mx2id=i,mx1id
                mx1id = i
            elif mx > mx2:
                mx2 = mx
                # mx2id=i

        if mx1id != mi1id:
            return mx1 - mi1
        else:
            return max(mx1 - mi2, mx2 - mi1)


# @lc code=end
assert Solution().maxDistance([[1], [1]]) == 0


#
# @lcpr case=start
# [[1,2,3],[4,5],[1,2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[1]]\n
# @lcpr case=end

#
