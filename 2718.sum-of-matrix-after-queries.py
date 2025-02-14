#
# @lc app=leetcode.cn id=2718 lang=python3
# @lcpr version=30204
#
# [2718] 查询后矩阵的和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        #1 set row
        #2 set col
        seted=[0]*n
        cnt=[0,0]
        ret=0
        for t,idx,val in reversed(queries):
            if seted[idx] & (1<<t):continue
            ret+=val*(n-cnt[t^1])
            cnt[t]+=1
            seted[idx]|=1<<t
        return ret
# @lc code=end
assert Solution().matrixSumQueries(n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]])==17
assert Solution().matrixSumQueries(n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]])==23


#
# @lcpr case=start
# 3\n[[0,0,1],[1,2,2],[0,2,3],[1,0,4]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]\n
# @lcpr case=end

#

