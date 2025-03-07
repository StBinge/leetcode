#
# @lc app=leetcode.cn id=3361 lang=python3
# @lcpr version=30204
#
# [3361] 两个字符串的切换距离
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:
        nextCost=[0]+nextCost
        previousCost=[0]+previousCost
        for i in range(1, 27):
            nextCost[i] += nextCost[i - 1]
            previousCost[i] += previousCost[i-1]

        ret = 0
        for x, y in zip(s, t):
            if x == y:
                continue
            x = ord(x) - 97
            y = ord(y) - 97
            nxt_val = pre_val = 0
            if x > y:
                nxt_val = nextCost[y]+nextCost[-1]-nextCost[x]
                pre_val = previousCost[x+1] - previousCost[y+1]
            elif x < y:
                nxt_val = nextCost[y]-nextCost[x]
                pre_val = previousCost[x+1]+previousCost[-1]-previousCost[y+1]
            ret += min(nxt_val, pre_val)

        return ret


# @lc code=end
assert Solution().shiftDistance(s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])==2
assert Solution().shiftDistance(s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])==31
#
# @lcpr case=start
# "abab"\n"baba"\n[100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]\n[1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# "leet"\n"code"\n[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]\n[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#
