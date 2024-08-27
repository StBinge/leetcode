#
# @lc app=leetcode.cn id=1913 lang=python3
# @lcpr version=30204
#
# [1913] 两个数对之间的最大乘积差
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx1=mx2=0
        mi1=mi2=10**5
        for n in nums:
            if n>mx1:
                mx1,mx2=n,mx1
            elif n>mx2:
                mx2=n
            
            if n<mi1:
                mi1,mi2=n,mi1
            elif n<mi2:
                mi2=n
        return mx1*mx2-mi1*mi2

# @lc code=end
assert Solution().maxProductDifference([5,6,2,7,4])==34


#
# @lcpr case=start
# [5,6,2,7,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,5,9,7,4,8]\n
# @lcpr case=end

#

