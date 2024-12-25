#
# @lc app=leetcode.cn id=2511 lang=python3
# @lcpr version=30204
#
# [2511] 最多可以摧毁的敌人城堡数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ret = 0
        pre = -1
        for i, f in enumerate(forts):
            if f != 0:
                if pre >= 0 and forts[i] != forts[pre]:
                    ret = max(ret, i - pre - 1)
                pre = i
        return ret


# @lc code=end


#
# @lcpr case=start
# [1,0,0,-1,0,0,0,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,-1]\n
# @lcpr case=end

#
