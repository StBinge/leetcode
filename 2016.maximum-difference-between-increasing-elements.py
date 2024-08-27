#
# @lc app=leetcode.cn id=2016 lang=python3
# @lcpr version=30204
#
# [2016] 增量元素之间的最大差值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mi=float('inf')
        ret=-1
        for n in nums:
            if n>mi:
                ret=max(ret,n-mi)
            else:
                mi=n
        return ret
# @lc code=end



#
# @lcpr case=start
# [7,1,5,4]\n
# @lcpr case=end

# @lcpr case=start
# [9,4,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,5,2,10]\n
# @lcpr case=end

#

