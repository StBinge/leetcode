#
# @lc app=leetcode.cn id=782 lang=python3
#
# [782] 变为棋盘
#
from typing import List
# @lc code=start
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n=len(board)
        row_mask=0
        col_mask=0
        for i in range(n):
            row_mask|=board[0][i]<<i
            col_mask|=board[i][0]<<i
        r_row_mask=((1<<n)-1)^row_mask
        r_col_mask=((1<<n)-1)^col_mask

        row_cnt=col_cnt=0
        for r in range(n):
            cur_row_mask=cur_col_mask=0
            for c in range(n):
                cur_row_mask|=board[r][c]<<c
                cur_col_mask|=board[c][r]<<c
            if (cur_col_mask!=col_mask and cur_col_mask!=r_col_mask) or (cur_row_mask!=row_mask and cur_row_mask!=r_row_mask):
                return -1
            if cur_col_mask==col_mask:
                col_cnt+=1
            if cur_row_mask==row_mask:
                row_cnt+=1

        if abs(n-2*row_cnt)>1 or abs(n-2*col_cnt)>1:
            return -1
        
        odd_mask=0x55555555#0101
        even_mask=0xAAAAAAAA#1010
        def get_moves(mask:int):
            nonlocal n
            ones=mask.bit_count()
            if abs(n-2*ones)>1:
                return -1
            if n&1:
                if ones==n//2:
                    return ones-(mask&even_mask).bit_count()
                else:
                    return ones-(mask&odd_mask).bit_count()
            else:
                return ones-max((mask&odd_mask).bit_count(),(mask&even_mask).bit_count())
        
        c1=get_moves(row_mask)
        if c1==-1:
            return -1
        c2=get_moves(col_mask)
        if c2==-1:
            return -1
        return c1+c2
# @lc code=end
board=[[0,0,1,0,1,1],[1,1,0,1,0,0],[1,1,0,1,0,0],[0,0,1,0,1,1],[1,1,0,1,0,0],[0,0,1,0,1,1]]
assert Solution().movesToChessboard(board)==2

board=[[1,1,0],[0,0,1],[0,0,1]]
assert Solution().movesToChessboard(board)==2

board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
assert Solution().movesToChessboard(board)==2
board = [[0, 1], [1, 0]]
assert Solution().movesToChessboard(board)==0
board = [[1, 0], [1, 0]]
assert Solution().movesToChessboard(board)==-1



