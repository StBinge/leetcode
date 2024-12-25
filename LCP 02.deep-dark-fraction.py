#
# @lc app=leetcode.cn id=LCP 02 lang=python3
# @lcpr version=30204
#
# [LCP 02] 分式化简
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        x,y=0,1
        for a in cont[::-1]:
            x,y=y,a*y+x
        return [y,x]

# @lc code=end
assert Solution().fraction([0,0,3])==[3,1]
assert Solution().fraction([3,2,0,2])==[13,4]


#
# @lcpr case=start
# [3, 2, 0, 2]\n
# @lcpr case=end

# @lcpr case=start
# [0, 0, 3]\n
# @lcpr case=end

#

