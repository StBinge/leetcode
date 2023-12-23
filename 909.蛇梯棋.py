#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#
from sbw import *
# @lc code=start
from collections import deque
# import heapq
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        transfer={}
        n=len(board)
        for r in range(n):
            for c in range(n):
                rr=n-1-r
                if board[rr][c]==-1:
                    continue
                if r%2:
                    cell=(r+1)*n-c
                else:
                    cell=r*n+c+1
                if cell==board[rr][c]:
                    continue
                transfer[cell]=board[rr][c]
        
        # q=[[-1,0]]
        q=deque([[0,1]])
        vis={1}
        target=n*n

        while q:
            # cell,step=heapq.heappop(q)
            step,cell=q.popleft()
            # cell=-cell
            if cell>=target:
                return step
            for i in range(cell+1,cell+6+1):
                nxt=i
                if i in transfer:
                    nxt=transfer[i]
                if nxt in vis:
                    continue
                q.append([step+1,nxt])
                # heapq.heappush(q,[-nxt,step+1])
                vis.add(nxt)
            nxt=cell+6
            if nxt in transfer or nxt in vis:
                continue
            q.append([step+1,nxt])
            vis.add(nxt)
        return -1
        # return -1 if ret==target else ret
# @lc code=end
board=[[-1,10,-1,15,-1],[-1,-1,18,2,20],[-1,-1,12,-1,-1],[2,4,11,18,8],[-1,-1,-1,-1,-1]]
assert Solution().snakesAndLadders(board)==3

board=[[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
assert Solution().snakesAndLadders(board)==2

board=[[1,1,-1],[1,1,1],[-1,1,1]]
assert Solution().snakesAndLadders(board)==-1

board = [[-1,-1],[-1,3]]
assert Solution().snakesAndLadders(board)==1

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
assert Solution().snakesAndLadders(board)==4
