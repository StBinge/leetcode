#
# @lc app=leetcode.cn id=2162 lang=python3
# @lcpr version=30204
#
# [2162] 设置时间的最少代价
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def calc(min,sec):
            if min>=100:
                return float('inf')
            s=str(min)+str(sec).rjust(2,'0')
            digits=list(map(int,s))
            while digits and digits[0]==0:
                digits.pop(0)
            ret=0
            cur=startAt
            for n in digits:
                if n!=cur:
                    ret+=moveCost
                    cur=n
                ret+=pushCost
            return ret
        minutes,seconds=divmod(targetSeconds,60)
        ret=calc(minutes,seconds)
        if minutes>0 and seconds+60<100:
            ret=min(ret,calc(minutes-1,seconds+60))
        return ret
            

# @lc code=end
assert Solution().minCostSetTime(1,9403,9402,6008)==65817
assert Solution().minCostSetTime(0,1,4,9)==5
assert Solution().minCostSetTime(startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76)==6


#
# @lcpr case=start
# 1\n2\n1\n600\n
# @lcpr case=end

# @lcpr case=start
# 0\n1\n2\n76\n
# @lcpr case=end

#

