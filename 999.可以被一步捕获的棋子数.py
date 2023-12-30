#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#
from sbw import *
# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ret=0
        for r in range(8):
            for c in range(8):
                if board[r][c]=='R':
                    nc=c+1
                    while nc<8:
                        if board[r][nc] =='B':
                            break
                        if board[r][nc]=='p':
                            ret+=1
                            break
                        nc+=1

                    nc=c-1
                    while nc>=0:
                        if board[r][nc] =='B':
                            break
                        if board[r][nc]=='p':
                            ret+=1
                            break
                        nc-=1

                    nr=r+1
                    while nr<8:
                        if board[nr][c] =='B':
                            break
                        if board[nr][c]=='p':
                            ret+=1
                            break
                        nr+=1

                    nr=r-1
                    while nr>=0:
                        if board[nr][c] =='B':
                            break
                        if board[nr][c]=='p':
                            ret+=1
                            break
                        nr-=1
                    return ret
# @lc code=end
board=[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
assert Solution().numRookCaptures(board)==0

board=[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
assert Solution().numRookCaptures(board)==3
