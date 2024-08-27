#
# @lc app=leetcode.cn id=1958 lang=python3
# @lcpr version=30204
#
# [1958] 检查操作是否合法
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        middle_color='W' if color=='B' else 'B'
        
        def expand(dir:list):
            nr,nc=rMove+dir[0],cMove+dir[1]
            if nr<0 or nr==8 or nc<0 or nr==8 or board[nr][nc]!=middle_color:
                return False
            nr+=dir[0]
            nc+=dir[1]
            while 0<=nr<8 and 0<=nc<8 and board[nr][nc]==middle_color:
                nr+=dir[0]
                nc+=dir[1]
            return 0<=nr<8 and 0<=nc<8 and board[nr][nc]==color
        
        can2right=cMove<6
        can2left=cMove>1
        can2up=rMove>1
        can2down=rMove<6

        hori=[0]
        if can2left:
            hori.append(-1)
        if can2right:
            hori.append(1)
        vert=[0]
        if can2up:
            vert.append(-1)
        if can2down:
            vert.append(1)
        for i in vert:
            for j in hori:
                if i==j==0:
                    continue
                if expand([i,j]):
                    return True
        return False



# @lc code=end
assert Solution().checkMove([["W","W",".","B",".","B","B","."],["W","B",".",".","W","B",".","."],["B","B","B","B","W","W","B","."],["W","B",".",".","B","B","B","."],["W","W","B",".","W",".","B","B"],["B",".","B","W",".","B",".","."],[".","B","B","W","B","B",".","."],["B","B","W",".",".","B",".","."]],7,4,"B")
assert Solution().checkMove(board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W")==False
assert Solution().checkMove([[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B")


#
# @lcpr case=start
# [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]]\n4\n3\n"B"\n
# @lcpr case=end

# @lcpr case=start
# [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]]\n4\n4\n"W"\n
# @lcpr case=end

#

