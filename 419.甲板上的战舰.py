#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#
from typing import List
# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ret=0
        R=len(board)
        C=len(board[0])
        # def erase(r,c):
            
        for r in range(R):
            for c in range(C):
                
                if board[r][c]=='X' and (r==0 or board[r-1][c]=='.') and (c==0 or board[r][c-1]=='.'):
                    ret+=1
                    
        return ret
# @lc code=end
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
assert Solution().countBattleships(board)==2
board = [["."]]
assert Solution().countBattleships(board)==0