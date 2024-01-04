#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        x,y=0,0
        dirs=[
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        d=0
        for i in range(len(instructions)):
            if instructions[i]=='L':
                d=(d+1)%4
            elif instructions[i]=='R':
                d=(d-1)%4
            else:
                x+=dirs[d][0]
                y+=dirs[d][1]
        return (x==0 and y==0) or d!=0

# @lc code=end
assert Solution().isRobotBounded('GG') ==False
