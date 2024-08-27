#
# @lc app=leetcode.cn id=1552 lang=python3
#
# [1552] 两球之间的磁力
#
from sbw import *


# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 0
        r = position[-1] - position[0]
        while l <= r:
            mid = (l + r) >> 1
            cnt = 1
            pre = position[0]
            for p in position[1:]:
                if p - pre >= mid:
                    cnt += 1
                    if cnt == m:
                        break
                    pre = p
            if cnt < m:
                r = mid-1
            else:
                l = mid + 1
        return r


# @lc code=end
assert Solution().maxDistance(position=[1, 2, 3, 4, 7], m=3) == 3
assert Solution().maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2) == 999999999
