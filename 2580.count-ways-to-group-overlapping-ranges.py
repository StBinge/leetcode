#
# @lc app=leetcode.cn id=2580 lang=python3
# @lcpr version=30204
#
# [2580] 统计将重叠区间合并成组的方案数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        segs=0
        pre_end=-1
        for start,end in ranges:
            if start>pre_end:
                segs+=1
            pre_end=max(end,pre_end)
        return pow(2,segs,10**9+7)
            
# @lc code=end
assert Solution().countWays([[1,3],[10,20],[2,5],[4,8]])==4
assert Solution().countWays([[6,10],[5,15]])==2


#
# @lcpr case=start
# [[6,10],[5,15]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[10,20],[2,5],[4,8]]\n
# @lcpr case=end

#

