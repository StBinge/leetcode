#
# @lc app=leetcode.cn id=3184 lang=python3
# @lcpr version=30204
#
# [3184] 构成整天的下标对数目 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt=defaultdict(int)
        ret=0
        for h in hours:
            m=h%24
            ret+=cnt[(24-m)%24]
            cnt[m]+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [12,12,30,24,24]\n
# @lcpr case=end

# @lcpr case=start
# [72,48,24,3]\n
# @lcpr case=end

#

