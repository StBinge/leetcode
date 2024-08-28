#
# @lc app=leetcode.cn id=2008 lang=python3
# @lcpr version=30204
#
# [2008] 出租车的最大盈利
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        f=[0]*(n+1)
        # rides.sort(key=lambda x:x[1])
        cache=defaultdict(list)
        for start,end,tip in rides:
            cache[end].append([start,end-start+tip])
        for i in range(1,n+1):
            f[i]=f[i-1]
            if i in cache:
                f[i]=max(f[i],max(f[s]+t for s,t in cache[i]))
        return f[-1]
# @lc code=end
assert Solution().maxTaxiEarnings(n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]])==20
assert Solution().maxTaxiEarnings(n = 5, rides = [[2,5,4],[1,5,1]])==7


#
# @lcpr case=start
# 5\n[[2,5,4],[1,5,1]]\n
# @lcpr case=end

# @lcpr case=start
# 20\n[[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]\n
# @lcpr case=end

#

