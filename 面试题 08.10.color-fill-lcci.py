#
# @lc app=leetcode.cn id=面试题 08.10 lang=python3
# @lcpr version=30204
#
# [面试题 08.10] 颜色填充
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color=image[sr][sc]
        if color==newColor:
            return image
        R,C=len(image),len(image[0])
        q=[[sr,sc]]
        while q:
            r,c=q.pop()
            image[r][c]=newColor
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if 0<=nr<R and 0<=nc<C and image[nr][nc]==color:
                    q.append([nr,nc])
        return image
# @lc code=end
assert Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]] ,sr = 1, sc = 1, newColor = 2)==[[2,2,2],[2,2,0],[2,0,1]]


#
# @lcpr case=start
# [[1,1,1],[1,1,0],[1,0\n1\n1\n2\n
# @lcpr case=end

#

