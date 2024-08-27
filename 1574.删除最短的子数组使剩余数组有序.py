#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#
from sbw import *


# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        r = N - 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        if r==0:
            return 0
        ret=r

        for i in range(N-1):
            while r<N and arr[r] < arr[i]:
                r+=1
            ret = min(ret, r - i - 1)
            if arr[i]>arr[i+1]:
                break
        return ret


# @lc code=end
assert Solution().findLengthOfShortestSubarray([10,13,17,21,15,15,9,17,22,22,13]) == 7
assert Solution().findLengthOfShortestSubarray([1]) == 0
assert Solution().findLengthOfShortestSubarray([1, 2, 3]) == 0
assert Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]) == 3
assert Solution().findLengthOfShortestSubarray([5, 4, 3, 2, 1]) == 4
