#
# @lc app=leetcode.cn id=2971 lang=python3
# @lcpr version=30204
#
# [2971] 找到最大周长的多边形
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s=sum(nums)
        for n in nums[::-1]:
            if n*2<s:
                return s
            s-=n
        return -1
# @lc code=end



#
# @lcpr case=start
# [5,5,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,12,1,2,5,50,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,50]\n
# @lcpr case=end

#

