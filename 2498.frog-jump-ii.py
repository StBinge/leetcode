#
# @lc app=leetcode.cn id=2498 lang=python3
# @lcpr version=30204
#
# [2498] 青蛙过河 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ret=stones[1]-stones[0]
        for i in range(2,len(stones)):
            ret=max(ret,stones[i]-stones[i-2])
        return ret
# @lc code=end



#
# @lcpr case=start
# [0,2,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,9]\n
# @lcpr case=end

#

