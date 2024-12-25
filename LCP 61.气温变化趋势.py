#
# @lc app=leetcode.cn id=LCP 61 lang=python3
# @lcpr version=30204
#
# [LCP 61] 气温变化趋势
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        ret=cur=0
        def get_dir(x,y):
            return (x>y) - (y>x)
        for i in range(1,len(temperatureA)):
            da=get_dir(temperatureA[i-1],temperatureA[i])
            db=get_dir(temperatureB[i-1],temperatureB[i])
            if da==db:
                cur+=1
            else:
                ret=max(ret,cur)
                cur=0
        return max(ret,cur)

        
# @lc code=end



#
# @lcpr case=start
# [21,18,18,18\n[34,32,16,16,17]`>\n
# @lcpr case=end

# @lcpr case=start
# [5,10,16,-6,15,11\n[16,22,23,23,25,3,-16]`>\n
# @lcpr case=end

#

