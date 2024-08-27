#
# @lc app=leetcode.cn id=1590 lang=python3
#
# [1590] 使数组和能被 P 整除
#
from sbw import *


# @lc code=start
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        if tot % p == 0:
            return 0
        M = tot % p
        N = len(nums)
        m = 0
        cache = {0:-1}
        ret = N
        for i in range(N):
            m = (m+nums[i])%p
            pair=(m-M)%p
            if pair in cache:
                ret = min(ret, i - cache[pair])
            cache[m] = i
        return -1 if ret == N else ret


# @lc code=end
assert Solution().minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2],148) == 7
assert Solution().minSubarray(nums=[1, 2, 3], p=7) == -1
assert Solution().minSubarray([4,4,2],7) == -1
assert Solution().minSubarray(nums=[1000000000, 1000000000, 1000000000], p=3) == 0
assert Solution().minSubarray(nums=[1, 2, 3], p=3) == 0
assert Solution().minSubarray(nums=[6, 3, 5, 2], p=9) == 2
assert Solution().minSubarray([3, 1, 4, 2], 6) == 1
