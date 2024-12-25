#
# @lc app=leetcode.cn id=2332 lang=python3
# @lcpr version=30204
#
# [2332] 坐上公交的最晚时间
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        N=len(buses)
        M=len(passengers)
        buses.sort()
        passengers.sort()
        pidx=0
        cnt=0
        for i in range(N):
            time=buses[i]
            cnt=capacity
            while pidx<M and cnt>0 and passengers[pidx]<=time:
                cnt-=1
                pidx+=1
           
        pidx-=1
        if cnt>0:
            time=buses[-1]
        else:
            time=passengers[pidx]
        
        while pidx>=0 and passengers[pidx]==time:
            time-=1
            pidx-=1
        return time


            

# @lc code=end
assert Solution().latestTimeCatchTheBus([20,30,10],[19,13,26,4,25,11,21],2)==20
assert Solution().latestTimeCatchTheBus([2],[2],2)==1
assert Solution().latestTimeCatchTheBus([5],[7,8],1)==5
assert Solution().latestTimeCatchTheBus([3],[2,4],2)==3
assert Solution().latestTimeCatchTheBus([10,20],[2,17,18,19],2)==16


#
# @lcpr case=start
# [10,20]\n[2,17,18,19]\n2\n
# @lcpr case=end

# @lcpr case=start
# [20,30,10]\n[19,13,26,4,25,11,21]\n2\n
# @lcpr case=end

#

