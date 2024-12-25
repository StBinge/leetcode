#
# @lc app=leetcode.cn id=2140 lang=python3
# @lcpr version=30204
#
# [2140] 解决智力问题
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N=len(questions)
        f=[0]*(N+1)
        # f[N-1]=questions[-1][0]
        for i in range(N-1,-1,-1):
            p,b=questions[i]
            f[i]=max(p+f[min(N,i+b+1)],f[i+1])
        return f[0]
# @lc code=end
assert Solution().mostPoints([[3,2],[4,3],[4,4],[2,5]])==5


#
# @lcpr case=start
# [[3,2],[4,3],[4,4],[2,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,2],[3,3],[4,4],[5,5]]\n
# @lcpr case=end

#

