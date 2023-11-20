#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#
from typing import List
# @lc code=start
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_cnt=0
        o_cnt=0
        for i in range(3):
            for j in range(3):
                if board[i][j]=='X':
                    x_cnt+=1
                elif board[i][j]=='O':
                    o_cnt+=1
        if x_cnt<o_cnt or x_cnt>o_cnt+1:
            return False
        
        def has_win(s:str):
            pat=s*3
            for i in range(3):
                if board[i]==pat:
                    return True
                for j in range(3):
                    if board[j][i]!=s:
                        break
                else:
                    return True
            if board[0][0]==board[1][1]==board[2][2]==s:
                return True
            if board[0][2]==board[1][1]==board[2][0]==s:
                return True
            return False

        o_win=has_win('O')
        x_win=has_win('X')
        if o_win and x_win:
            return False
        if o_win and x_cnt!=o_cnt:
            return False
        if x_win and x_cnt-1!=o_cnt:
            return False
        return True
# @lc code=end
board=["XOX","OX ","OXO"]
assert Solution().validTicTacToe(board)

board=["XXX","OOX","OOX"]
assert Solution().validTicTacToe(board)

board = ["O  ","   ","   "]
assert Solution().validTicTacToe(board)==False
board = ["XOX"," X ","   "]
assert Solution().validTicTacToe(board)==False
board = ["XOX","O O","XOX"]
assert Solution().validTicTacToe(board)
