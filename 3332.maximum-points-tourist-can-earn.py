#
# @lc app=leetcode.cn id=3332 lang=python3
# @lcpr version=30204
#
# [3332] 旅客可以得到的最多点数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        f=[[0]*n for _ in range(k+1)]
        for i in range(k):
            for j in range(n):
                f[i+1][j]=max(f[i+1][j],f[i][j]+stayScore[i][j])
                for j2 in range(n):
                    f[i+1][j]=max(f[i+1][j],f[i][j2]+travelScore[j2][j])
        return max(f[-1])

# @lc code=end
assert Solution().maxScore(1,1,[[1]],[[0]])==1
assert Solution().maxScore(n = 3, k = 2, stayScore = [[3,4,2],[2,1,2]], travelScore = [[0,2,1],[2,0,4],[3,2,0]])==8
assert Solution().maxScore(n = 2, k = 1, stayScore = [[2,3]], travelScore = [[0,2],[1,0]])==3


#
# @lcpr case=start
# 2\n1\n[[2,3]]\n[[0,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n[[3,4,2],[2,1,2]]\n[[0,2,1],[2,0,4],[3,2,0]]\n
# @lcpr case=end

#

