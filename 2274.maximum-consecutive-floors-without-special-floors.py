#
# @lc app=leetcode.cn id=2274 lang=python3
# @lcpr version=30204
#
# [2274] 不含特殊楼层的最大连续楼层数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.append(bottom-1)
        special.append(top+1)
        special.sort()
        ret=0
        for i in range(len(special)-1):
            ret=max(special[i+1]-special[i]-1,ret)
        return ret
# @lc code=end



#
# @lcpr case=start
# 2\n9\n[4,6]\n
# @lcpr case=end

# @lcpr case=start
# 6\n8\n[7,6,8]\n
# @lcpr case=end

#

