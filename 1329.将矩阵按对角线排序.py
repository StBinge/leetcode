#
# @lc app=leetcode.cn id=1329 lang=python3
#
# [1329] 将矩阵按对角线排序
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R,C=len(mat),len(mat[0])
        if R==1 or C==1:
            return mat
        dialines=[[] for _ in range((R+C-1))]
        for r in range(R):
            for c in range(C):
                heapq.heappush(dialines[r-c+C-1],mat[r][c])
        
        ret=[[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                ret[r][c]=heapq.heappop(dialines[r-c+C-1])
        return ret


# @lc code=end
assert Solution().diagonalSort([[3,9],[2,4],[1,2],[9,8],[7,3]])==[[3,9],[2,4],[1,2],[3,8],[7,9]]
assert Solution().diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]])==[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
assert Solution().diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]])==[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
assert Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])==[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
