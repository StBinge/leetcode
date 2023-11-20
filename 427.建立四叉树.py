#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#
from typing import List
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
# @lc code=start
"""
# Definition for a QuadTree node.
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N=len(grid)
        presum=[[0]*(N+1) for _ in range(N+1)]
        for i in range(N):
            for j in range(N):
                presum[i+1][j+1]=grid[i][j]+presum[i+1][j]+presum[i][j+1]-presum[i][j]

        def get_area(x1,y1,x2,y2):
            return presum[x2+1][y2+1]-presum[x2+1][y1]-presum[x1][y2+1]+presum[x1][y1]
        
        def build(x1,y1,x2,y2)->Node:
            area=get_area(x1,y1,x2,y2)
            if area==0:
                return Node(0,True,None,None,None,None)
            elif area==(x2-x1+1)*(y2-y1+1):
                return Node(1,True,None,None,None,None)
            
            midx=(x1+x2)//2
            midy=(y1+y2)//2
            left_top=build(x1,y1,midx,midy)
            left_bottom=build(midx+1,y1,x2,midy)
            right_top=build(x1,midy+1,midx,y2)
            right_bottom=build(midx+1,midy+1,x2,y2)
            # if (left_top.isLeaf and left_bottom.isLeaf and right_top.isLeaf and right_bottom.isLeaf) and left_top.val==left_bottom.val==right_top.val==right_bottom.val:
            #     return Node(left_top.val,True,None,None,None,None)
            return Node(1,False,left_top,right_top,left_bottom,right_bottom)
   
        return build(0,0,N-1,N-1)
# @lc code=end
# grid=[[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,1]]
# r=(Solution().construct(grid))

grid = [[0,1],[1,0]]
r=(Solution().construct(grid))

grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
r=(Solution().construct(grid))
pass