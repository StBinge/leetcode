#
# @lc app=leetcode.cn id=2100 lang=python3
# @lcpr version=30204
#
# [2100] 适合野炊的日子
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N=len(security)
        f_desc=[1]*N
        f_asc=[1]*N
        for i in range(1,N):
            if security[i-1]>=security[i]:
                f_desc[i]+=f_desc[i-1]
        
            if security[i-1]<=security[i]:
                f_asc[i]+=f_asc[i-1]
        ret=[]
        for i in range(time,N-time):
            if f_desc[i]>time and f_asc[i+time]>time:
                ret.append(i)
        return ret
# @lc code=end
assert Solution().goodDaysToRobBank(security = [5,3,3,3,5,6,2], time = 2)==[2,3]


#
# @lcpr case=start
# [5,3,3,3,5,6,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n2\n
# @lcpr case=end

#

