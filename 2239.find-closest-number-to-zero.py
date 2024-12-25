#
# @lc app=leetcode.cn id=2239 lang=python3
# @lcpr version=30204
#
# [2239] 找到最接近 0 的数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mx_dist=10**5
        ret=-10**5
        for n in nums:
            if abs(n)<mx_dist:
                mx_dist=abs(n)
                ret=n
            elif abs(n)==mx_dist:
                ret=max(ret,n)
        return ret
# @lc code=end



#
# @lcpr case=start
# [-4,-2,1,4,8]\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,1]\n
# @lcpr case=end

#

