#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#
from typing import List
# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        cx,cy=click
        if board[cx][cy]=='M':
            board[cx][cy]='X'
            return board
        R,C=len(board),len(board[0])
        counter={}
        dirs=[-1,0,1]
        for r in range(R):
            for c in range(C):
                if board[r][c]=='M':
                    for i in dirs:
                        for j in dirs:
                            if i==0 and j==0:
                                continue
                            x,y=r+i,c+j
                            # print(x,y)
                            if 0<=x<R and 0<=y<C:
                                idx=x*C+y
                                cnt=counter.get(idx,0)+1
                                counter[idx]=cnt
       
        c=counter.get(cx*C+cy,0)
        board[cx][cy]=str(c) if c else 'B'
        if c:
            return board
        empties=[[cx,cy]]
      
        while empties:
            temp=[]
            for r,c in empties:              
                for i in dirs:
                    for j in dirs:
                        x,y=r+i,c+j
                        if 0<=x<R and 0<=y<C and board[x][y]=='E':
                            idx=x*C+y
                            if idx in counter:
                                board[x][y]=str(counter[idx])
                                continue
                            board[x][y]='B'
                            temp.append([x,y])
            empties=temp
        return board

# @lc code=end
board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
assert Solution().updateBoard(board,click)==[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
click = [1,2]
assert Solution().updateBoard(board,click)==[["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

board=[["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","M"],["E","E","M","E","E","E","E","E"],["M","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]
click=[0,0]
assert Solution().updateBoard(board,click)==[["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","2","M","1","B","B","1","1"],["M","2","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]]
