#
# @lc app=leetcode.cn id=1819 lang=python3
#
# [1819] 序列中不同最大公约数的数目
#
from sbw import *


# @lc code=start
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # cnt = [0] * (max(nums) + 1)
        Max = max(nums)
        has = [False] * (Max + 1)
        ret = 0
        for n in nums:
            if not has[n]:
                has[n] = True
                ret+=1
        for i in range(1, Max//3 + 1):
            if has[i]:
                continue
            g = 0
            for j in range(i*2, Max + 1, i):
                if has[j]:
                    g = math.gcd(g, j)
                    if g == i:
                        ret += 1
                        break
        return ret


# @lc code=end
assert Solution().countDifferentSubsequenceGCDs([13, 7, 4, 16, 1]) == 5
assert Solution().countDifferentSubsequenceGCDs([16, 15]) == 3
assert Solution().countDifferentSubsequenceGCDs([5, 15, 40, 5, 6]) == 7
assert Solution().countDifferentSubsequenceGCDs([6, 10, 3]) == 5
