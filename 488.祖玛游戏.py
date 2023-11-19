#
# @lc app=leetcode.cn id=488 lang=python3
#
# [488] 祖玛游戏
#

# @lc code=start
# from queue import Queue
from collections import deque
import re
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s:str):
            n=1
            while n:
                s,n=re.subn(r'(.)\1{2,}','',s)
            return s
        
        hand=''.join(sorted(hand))
        queue=deque()
        queue.append([board,hand,0])
        visited={(board,hand)}
        while queue:
            board,hand,step=queue.popleft()
            for i in range(len(board)+1):
                for j in range(len(hand)):
                    if i>0 and board[i-1]==hand[j]:
                        continue
                    if j>0 and hand[j-1]==hand[j]:
                        continue
                    
                    choose=i<len(board) and board[i]==hand[j]
                    if not choose:
                        choose=0<i<len(board) and board[i-1]==board[i] and board[i]!=hand[j]
                    if choose:
                        new_board=clean(board[:i]+hand[j]+board[i:])
                        if not new_board:
                            return step+1
                        new_hand=hand[:j]+hand[j+1:]
                        if (new_board,new_hand) not in visited:
                            queue.append([new_board,new_hand,step+1])
                            visited.add((new_board,new_hand))
        return -1
        
# @lc code=end
board = "RYYRRYYRYRYYRYYR"
hand = "RRRRR"
assert Solution().findMinStep(board,hand)==5

board = "WRRBBW"
hand = "RB"
assert Solution().findMinStep(board,hand)==-1

board = "WWRRBBWW"
hand = "WRBRW"
assert Solution().findMinStep(board,hand)==2

board = "G"
hand = "GGGGG"
assert Solution().findMinStep(board,hand)==2

board = "RBYYBBRRB"
hand = "YRBGB"
assert Solution().findMinStep(board,hand)==3