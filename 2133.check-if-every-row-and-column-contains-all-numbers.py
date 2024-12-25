#
# @lc app=leetcode.cn id=2133 lang=python3
# @lcpr version=30204
#
# [2133] 检查是否每一行每一列都包含全部整数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N=len(matrix)
        cnt=[0]*(N+1)
        for i,row in enumerate(matrix):
            for v in row:
                # v出现的次数应该等于当前的行数
                if cnt[v]!=i:
                    return False
                cnt[v]+=1
        
        for j in range(N):
            for row in matrix:
                v=row[j]
                # v出现的次数应该等于N+当前的列数
                if cnt[v]!=N+j:
                    return False
                cnt[v]+=1
        return True
# @lc code=end
assert Solution().checkValid([[1,1,1],[1,2,3],[1,2,3]])==False
assert Solution().checkValid([[1,2,3],[3,1,2],[2,3,1]])


#
# @lcpr case=start
# [[1,2,3],[3,1,2],[2,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[1,2,3],[1,2,3]]\n
# @lcpr case=end

#

