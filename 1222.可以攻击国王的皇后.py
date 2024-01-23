#
# @lc app=leetcode.cn id=1222 lang=python3
#
# [1222] 可以攻击国王的皇后
#
from sbw import *
# @lc code=start
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        pos=set(map(tuple,queens))
        ret=[]
        dirs=[
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
            [1,1],
            [-1,-1],
            [-1,1],
            [1,-1]
        ]
        for x,y in dirs:
            r,c=king
            r+=x
            c+=y
            while 0<=r<8 and 0<=c<8:
                if (r,c) in pos:
                    ret.append([r,c])
                    break
                r+=x
                c+=y
        return ret

# @lc code=end
assert sorted(Solution().queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))==sorted([[2,2],[3,4],[4,4]])
assert sorted(Solution().queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))==sorted([[0,1],[1,0],[3,3]])
