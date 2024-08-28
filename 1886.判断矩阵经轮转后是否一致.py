#
# @lc app=leetcode.cn id=1886 lang=python3
#
# [1886] 判断矩阵经轮转后是否一致
#
from sbw import *


# @lc code=start
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        N = len(mat)
        center = (N - 1) / 2

        def map(flag, x, y):
            if flag == 0:
                return x, y
            x, y = x - center, y - center
            if flag == 1:
                return y + center, -x + center
            if flag == 2:
                return -x + center, -y + center
            if flag == 3:
                return -y + center, x + center

        for i in range(4):
            for r in range(N):
                valid = True
                for c in range(N):
                    rr, cc = map(i, r, c)
                    if mat[int(rr)][int(cc)] != target[r][c]:
                        valid = False
                        break
                if not valid:
                    break
            else:
                return True
        return False


# @lc code=end
assert Solution().findRotation(
    mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]
)
assert Solution().findRotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]) == False
assert Solution().findRotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]])
