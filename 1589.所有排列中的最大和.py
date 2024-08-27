#
# @lc app=leetcode.cn id=1589 lang=python3
#
# [1589] 所有排列中的最大和
#
from sbw import *


# @lc code=start
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        N = len(nums)
        dif = [0] * (N + 1)
        for s, e in requests:
            dif[s] += 1
            dif[e + 1] -= 1
        cnt = [0] * N
        cur=0
        for i in range(N):
            cur += dif[i]
            cnt[i] = cur
        cnt.sort(reverse=True)
        ret = 0
        for c, n in zip(cnt, nums):
            if c == 0:
                break
            ret += c * n
            ret%=(10**9+7)
        return ret


# @lc code=end
assert (
    Solution().maxSumRangeQuery(nums = [1,2,3,4,5,6], requests = [[0,1]]) == 11
)
assert (
    Solution().maxSumRangeQuery(nums=[1, 2, 3, 4, 5], requests=[[1, 3], [0, 1]]) == 19
)
