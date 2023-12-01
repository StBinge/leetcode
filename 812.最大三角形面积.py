#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#
from typing import List
# @lc code=start
class Solution:
    
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def get_convex_hull(points:list):
            def cross(p,q,r):
                return (q[0]-p[0])*(r[1]-q[1])-(q[1]-p[1])*(r[0]-q[0])
            if len(points)<4:
                return points
            points.sort()
            hull=[]
            for p in points:
                while len(hull)>1 and cross(hull[-2],hull[-1],p)<=0:
                    hull.pop()
                hull.append(p)
            m=len(hull)
            for i in range(len(points)-2,-1,-1):
                while len(hull)>m and cross(hull[-2],hull[-1],points[i])<=0:
                    hull.pop()
                hull.append(points[i])
            hull.pop()
            return hull
        
        def area(p1,p2,p3):
            return abs(p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]-p1[0]*p3[1]-p2[0]*p1[1]-p3[0]*p2[1])/2

        hull=get_convex_hull(points)
        n=len(hull)
        ret=0
        for i in range(n-2):
            p1=hull[i]
            k=i+2
            for j in range(i+1,n-1):
                p2=hull[j]
                cur=0
                while k<n:
                    nxt=area(p1,p2,hull[k])
                    if nxt<=cur:
                        break
                    cur=nxt
                    k+=1
                k-=1
                ret=max(ret,cur)
        return ret
# @lc code=end
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
assert Solution().largestTriangleArea(points)==2
points = [[1,0],[0,0],[0,1]]
assert Solution().largestTriangleArea(points)==0.5

