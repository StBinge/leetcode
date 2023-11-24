#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
from typing import List
# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        invalid_set=set(map(tuple,obstacles))
        # if (0,0) in invalid_set:
        #     return 0
        dirs=[
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        dir_idx=0
        pos=[0,0]
        ret=0
        for cmd in commands:
            if cmd==-2:
                dir_idx=(dir_idx-1)%4
            elif cmd==-1:
                dir_idx=(dir_idx+1)%4
            else:
                copy_x,copy_y=pos
                dir_x,dir_y=dirs[dir_idx]
                for i in range(cmd):
                    nxt=[0,0]
                    nxt[0]=pos[0]+dir_x
                    nxt[1]=pos[1]+dir_y
                    if tuple(nxt) in invalid_set:
                        break
                    pos=nxt
                    if abs(pos[0])>abs(copy_x) or abs(pos[1])>abs(copy_y):
                        ret=max(ret,pos[0]**2 + pos[1]**2)
        return ret
# @lc code=end
commands = [-2,-1,-2,3,7]
obstacles = [[1,-3],[2,-3],[4,0],[-2,5],[-5,2],[0,0],[4,-4],[-2,-5],[-1,-2],[0,2]]
assert Solution().robotSim(commands,obstacles)==100

commands = [7,-2,-2,7,5]
obstacles = [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]
assert Solution().robotSim(commands,obstacles)==4

commands = [6,-1,-1,6]
obstacles = []
assert Solution().robotSim(commands,obstacles)==36

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
assert Solution().robotSim(commands,obstacles)==65

commands = [4,-1,3]
obstacles = []
assert Solution().robotSim(commands,obstacles)==25