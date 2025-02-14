#
# @lc app=leetcode.cn id=2513 lang=python3
# @lcpr version=30204
#
# [2513] 最小化两个数组中的最大值
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizeSet(
        self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int
    ) -> int:
        lcm = math.lcm(divisor2, divisor1)
        left=uniqueCnt2+uniqueCnt1
        right=(uniqueCnt1+uniqueCnt2)*2-1

        def check(x):
            banned=x//lcm
            only1=x//divisor2-banned
            only2=x//divisor1-banned
            share=x-x//divisor1-x//divisor2+banned
            return share>=max(uniqueCnt1-only1,0)+max(uniqueCnt2-only2,0)

        return bisect_left(range(right),True,key=check)


# @lc code=end

assert Solution().minimizeSet(divisor1=2, divisor2=4, uniqueCnt1=8, uniqueCnt2=2) == 15
assert Solution().minimizeSet(divisor1=3, divisor2=5, uniqueCnt1=2, uniqueCnt2=1) == 3
assert Solution().minimizeSet(divisor1=2, divisor2=7, uniqueCnt1=1, uniqueCnt2=3) == 4

#
# @lcpr case=start
# 2\n7\n1\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n5\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# 2\n4\n8\n2\n
# @lcpr case=end

#
