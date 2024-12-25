#
# @lc app=leetcode.cn id=3096 lang=python3
# @lcpr version=30204
#
# [3096] 得到更多分数的最少关卡数目
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        # presums=[0]
        # for p in possible:
        #     presums.append(presums[-1]+p*2-1)
        s=sum(p*2-1 for p in possible)
        cur=0
        for i in range(len(possible)-1):
            cur+=possible[i]*2-1
            if cur*2>s:
                return i+1
        return -1

# @lc code=end



#
# @lcpr case=start
# [1,0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n
# @lcpr case=end

#

