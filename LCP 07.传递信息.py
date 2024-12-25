#
# @lc app=leetcode.cn id=LCP 07 lang=python3
# @lcpr version=30204
#
# [LCP 07] 传递信息
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        f0=[0]*n
        f0[0]=1
        for i in range(k):
            f1=[0]*n
            for x,y in relation:
                f1[y]+=f0[x]
            f0=f1
        return f0[-1]
            
# @lc code=end
assert Solution().numWays(n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3)==3


#
# @lcpr case=start
# 5\n[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,2],[2,1]]\n2\n
# @lcpr case=end

#

