#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up=left=0
        for d in moves:
            if d=='U':
                up+=1
            elif d=='D':
                up-=1
            elif d=='L':
                left+=1
            else:
                left-=1
        return up==left==0
# @lc code=end

