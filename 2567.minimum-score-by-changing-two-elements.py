#
# @lc app=leetcode.cn id=2567 lang=python3
# @lcpr version=30204
#
# [2567] 修改两个元素的最小分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        mi0=mi1=mi2=float('inf')
        mx0=mx1=mx2=float('-inf')
        for n in nums:
            if n<mi0:
                mi0,mi1,mi2=n,mi0,mi1
            elif n<mi1:
                mi1,mi2=n,mi1
            elif n<mi2:
                mi2=n
            
            if n>mx0:
                mx0,mx1,mx2=n,mx0,mx1
            elif n>mx1:
                mx1,mx2=n,mx1
            elif n>mx2:
                mx2=n
        
        return min(mx0-mi2,mx2-mi0,mx1-mi1)
# @lc code=end
assert Solution().minimizeSum([31,25,72,79,74,65])==14


#
# @lcpr case=start
# [1,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,7,8,5]\n
# @lcpr case=end

#

