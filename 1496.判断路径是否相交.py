#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        vis={(0,0)}
        x,y=0,0
        for d in path:
            if d=='N':
                y+=1
            elif d=='S':
                y-=1
            elif d=='E':
                x+=1
            elif d=='W':
                x-=1
            if (x,y) in vis:
                return True
            vis.add((x,y))
        return False
# @lc code=end

