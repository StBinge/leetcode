#
# @lc app=leetcode.cn id=1712 lang=python3
#
# [1712] 将数组分成三个子数组的方案数
#
from sbw import *


# @lc code=start
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        N = len(nums)
        sm = list(accumulate(nums, initial=0))
        l1, l2 = 1, 1
        ret = 0
        for r in range(2, N):

            while l1<r and sm[l1]<=sm[r]-sm[l1]:
                l1+=1

            while l2<l1 and sm[r]-sm[l2]>sm[N]-sm[r]:
                l2 += 1
            ret += l1 - l2
        return ret % (10**9 + 7)





# @lc code=end
assert (
    Solution().waysToSplit(
        [
            8892,
            2631,
            7212,
            1188,
            6580,
            1690,
            5950,
            7425,
            8787,
            4361,
            9849,
            4063,
            9496,
            9140,
            9986,
            1058,
            2734,
            6961,
            8855,
            2567,
            7683,
            4770,
            40,
            850,
            72,
            2285,
            9328,
            6794,
            8632,
            9163,
            3928,
            6962,
            6545,
            6920,
            926,
            8885,
            1570,
            4454,
            6876,
            7447,
            8264,
            3123,
            2980,
            7276,
            470,
            8736,
            3153,
            3924,
            3129,
            7136,
            1739,
            1354,
            661,
            1309,
            6231,
            9890,
            58,
            4623,
            3555,
            3100,
            3437,
        ]
    )
    == 227
)
assert Solution().waysToSplit([0, 3, 3]) == 1
assert Solution().waysToSplit([3, 2, 1]) == 0
assert Solution().waysToSplit([1, 2, 2, 2, 5, 0]) == 3
assert Solution().waysToSplit([1, 1, 1]) == 1
