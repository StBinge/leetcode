#
# @lc app=leetcode.cn id=1926 lang=python3
# @lcpr version=30204
#
# [1926] 迷宫中离入口最近的出口
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        R,C=len(maze),len(maze[0])

        r,c=entrance
        maze[r][c]='+'
        q=deque([[r,c,0]])
        while q:
            r,c,step=q.popleft()
            maze[r][c]='+'
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if 0<=nr<R and 0<=nc<C:
                    if maze[nr][nc]=='.':
                        q.append([nr,nc,step+1])
                        maze[nr][nc]="+"
                else:
                    if step:
                        return step
        return -1
# @lc code=end
assert Solution().nearestExit(maze = [[".","+"]], entrance = [0,0])==-1
assert Solution().nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0])==2
assert Solution().nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2])==1


#
# @lcpr case=start
# [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# [["+","+","+"],[".",".","."],["+","+","+"]]\n[1,0]\n
# @lcpr case=end

# @lcpr case=start
# [[".","+"]]\n[0,0]\n
# @lcpr case=end

#

