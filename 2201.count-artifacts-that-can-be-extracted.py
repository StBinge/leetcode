#
# @lc app=leetcode.cn id=2201 lang=python3
# @lcpr version=30204
#
# [2201] 统计可以提取的工件
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        digs=set(r*n+c for r,c in dig)
        ret=0
        for r1,c1,r2,c2 in artifacts:
            found=True
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    if r*n+c not in digs:
                        found=False
                        break
                if not found:
                    break
            if found:
                ret+=1
        return ret
# @lc code=end
assert Solution().digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]])==2
assert Solution().digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]])==1


#
# @lcpr case=start
# 2\n[[0,0,0,0],[0,1,1,1]]\n[[0,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,0,0,0],[0,1,1,1]]\n[[0,0],[0,1],[1,1]]\n
# @lcpr case=end

#

