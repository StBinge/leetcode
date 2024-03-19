#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#
from sbw import *
# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves)<5:
            return 'Pending'
        cnt=[[[0]*3,[0]*3,[0]*2] for _ in range(2)]
        for i, [r,c] in enumerate(moves):
            rows,cols,dias=cnt[i%2]
            rows[r]+=1
            cols[c]+=1
            if r==c:
                dias[0]+=1
            if r+c==2:
                dias[1]+=1
        for i,c in enumerate(cnt):
            for cc in c:
                for ccc in cc:
                    if ccc==3:
                        return 'A' if i==0 else 'B'
        return 'Draw' if len(moves)==9 else 'Pending'


# @lc code=end
assert Solution().tictactoe([[0,0],[1,1]])=='Pending'
assert Solution().tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])=='Draw'
assert Solution().tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])=='B'
assert Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])=='A'
