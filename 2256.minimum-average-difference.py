#
# @lc app=leetcode.cn id=2256 lang=python3
# @lcpr version=30204
#
# [2256] 最小平均差
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        s = sum(nums)
        left = 0
        mi = float("inf")
        ret = -1
        for i in range(N - 1):
            n = nums[i]
            left += n
            s -= n
            dif = abs(left // (i + 1) - s // (N - i - 1))
            if dif < mi:
                mi = dif
                ret = i
        if mi > (left+s)//N:
            return N - 1
        return ret


# @lc code=end
assert Solution().minimumAverageDifference([1,2,3,4,5]) == 0
assert Solution().minimumAverageDifference([0,1,0,1,0,1]) == 0
assert Solution().minimumAverageDifference([0, 0, 0, 0]) == 0


#
# @lcpr case=start
# [2,5,3,9,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
