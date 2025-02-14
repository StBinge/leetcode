#
# @lc app=leetcode.cn id=1742 lang=python3
# @lcpr version=30204
#
# [1742] 盒子中小球的最大数量
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt=defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            idx=sum(map(int,str(i)))
            cnt[idx]+=1
        return max(cnt.values())
# @lc code=end



#
# @lcpr case=start
# 1\n10\n
# @lcpr case=end

# @lcpr case=start
# 5\n15\n
# @lcpr case=end

# @lcpr case=start
# 19\n28\n
# @lcpr case=end

#

