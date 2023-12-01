#
# @lc app=leetcode.cn id=825 lang=python3
#
# [825] 适龄的朋友
#
from typing import List
# @lc code=start
import bisect
# from collections import coutner


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        L = len(ages)
        ret = 0
        left, right = 0, 0
        for age in ages:
            if age < 15:
                continue
            low = age/2+7
            while ages[left] <= low:
                left += 1
            while right+1 < L and ages[right+1] <= age:
                right += 1
            ret += right-left
        return ret


# @lc code=end
ages = [54, 23, 102, 90, 40, 74, 112, 74, 76, 21]
ret = 22
assert Solution().numFriendRequests(ages) == ret

ages = [101, 56, 69, 48, 30]
ret = 4
assert Solution().numFriendRequests(ages) == ret

ages = [20, 30, 100, 110, 120]
ret = 3
assert Solution().numFriendRequests(ages) == ret

ages = [16, 17, 18]
ret = 2
assert Solution().numFriendRequests(ages) == ret

ages = [16, 16]
assert Solution().numFriendRequests(ages) == 2
