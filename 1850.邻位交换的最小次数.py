#
# @lc app=leetcode.cn id=1850 lang=python3
#
# [1850] 邻位交换的最小次数
#
from sbw import *


# @lc code=start
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        N = len(num)

        def next_num(nums: list):
            i = N - 2
            while nums[i] >= nums[i + 1]:
                i -= 1
            j = N - 1
            while nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            left = i + 1
            right = N - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        nums = list(num)
        for _ in range(k):
            next_num(nums)

        ret = 0
        for i in range(N):
            if nums[i] == num[i]:
                continue
            for j in range(i + 1, N):
                if nums[j] == num[i]:
                    for k in range(j - 1, i - 1, -1):
                        nums[k], nums[k + 1] = nums[k + 1], nums[k]
                        ret += 1
                    break
        return ret


# @lc code=end
assert Solution().getMinSwaps("00123", 1) == 1
assert Solution().getMinSwaps("11112", 4) == 4
assert Solution().getMinSwaps("5489355142", 4) == 2
