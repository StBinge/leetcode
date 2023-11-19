#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
from typing import List
# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # hash=lambda r,c:r*201+c
        R=len(matrix)
        C=len(matrix[0])
        degrees=[[0]*C for _ in range(R)]

        Dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        queue=[]
        for r in range(R):
            for c in range(C):
                for x,y in Dirs:
                    rr=r+x
                    cc=c+y
                    if 0<=rr<R and 0<=cc<C and matrix[rr][cc]>matrix[r][c]:
                        degrees[r][c]+=1
                if degrees[r][c]==0:
                    queue.append([r,c])
        steps=0
        while queue:
            steps+=1
            temp=[]
            for r,c in queue:
                for x,y in Dirs:
                    rr=r+x
                    cc=c+y
                    if 0<=rr<R and 0<=cc<C and matrix[r][c]>matrix[rr][cc]:
                        degrees[rr][cc]-=1
                        if degrees[rr][cc]==0:
                            temp.append([rr,cc])
            queue=temp
        return steps

# @lc code=end

matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
assert Solution().longestIncreasingPath(matrix)==140


matrix = [[9,9,4],[6,6,8],[2,1,1]]
assert Solution().longestIncreasingPath(matrix)==4

matrix = [[3,4,5],[3,2,6],[2,2,1]]
assert Solution().longestIncreasingPath(matrix)==4

matrix = [[1]]
assert Solution().longestIncreasingPath(matrix)==1
