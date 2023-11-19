#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # step=0
        Neibours=[
            [1,3],
            [0,2,4],
            [1,5],
            [0,4],
            [3,1,5],
            [2,4]
        ]
        visited=set()
        queue=deque()
        initial=''.join(''.join(map(str,row)) for row in board)
        queue.append([initial,0])
        
        def get_next(pattern:str):
            board=list(pattern)
            x=pattern.index('0')
            for y in Neibours[x]:
                board[x],board[y]=board[y],board[x]
                yield ''.join(board)
                board[x],board[y]=board[y],board[x]


        visited.add(initial)
        while queue:
            pattern,step=queue.popleft()
            if pattern=='123450':
                return step
            for nxt in get_next(pattern):
                if nxt in visited:
                    continue
                visited.add(nxt)
                queue.append([nxt,step+1])
        return -1

# @lc code=end
board = [[4,1,2],[5,0,3]]
assert Solution().slidingPuzzle(board)==5
board = [[1,2,3],[4,0,5]]
assert Solution().slidingPuzzle(board)==1
board = [[1,2,3],[5,4,0]]
assert Solution().slidingPuzzle(board)==-1
