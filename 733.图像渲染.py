#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
from typing import List
# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c=image[sr][sc]
        if c==color:
            return image
        R=len(image)
        C=len(image[0])
        stack=[[sr,sc]]
        dirs=[-1,0,1,0,-1]
        while stack:
            x,y=stack.pop()
            image[x][y]=color
            for i in range(4):
                nx,ny=x+dirs[i],y+dirs[i+1]
                if nx<0 or nx==R or ny<0 or ny==C or image[nx][ny]!=c:
                    continue
                stack.append([nx,ny])
        return image
# @lc code=end

