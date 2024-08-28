#
# @lc app=leetcode.cn id=1610 lang=python3
#
# [1610] 可见点的最大数目
#
from sbw import *
# @lc code=start
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        east=[1,0]
        angles=[]
        same=0
        lx,ly=location
        for x,y in points:
            if [x,y]==location:
                same+=1
                continue
            angles.append(math.atan2(y-ly,x-lx))
            
        angles.sort()
        angles+=[d+2*math.pi for d in angles]
        angle=math.radians(angle)
        cnt=0
        left=0
        N=len(angles)
        for r in range(N):
            while angles[r%N]-angles[left%N]>angle:
                left+=1
            cnt=max(cnt,r-left+1)
        return cnt+same

# @lc code=end

assert Solution().visiblePoints(points = [[1,0],[2,1]], angle = 13, location = [1,1])==1
assert Solution().visiblePoints(points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1])==4
assert Solution().visiblePoints(points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1])==3