#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#
from typing import List
# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R=len(heights)
        C=len(heights[0])
        ret=[]
        visited=[[0]*C for _ in range(R)]

        # flow_top_left=0b01
        # flow_bottom_right=0b10
        # both_flow=0b11
        def mark(r,c,flag):
            nonlocal R,C
            visited[r][c]|=flag
            dirs=[-1,0,1,0,-1]
            # to_p,to_a=False,False
            for k in range(4):
                nr,nc=r+dirs[k],c+dirs[k+1]
                if nr<0 or nr>=R or nc<0 or nc>=C or visited[nr][nc] & flag==flag:
                    continue
                if heights[nr][nc]>=heights[r][c]:
                    mark(nr,nc,flag)
        
        pacific=[[0,c] for c in range(C)]+[[r,0] for r in range(R)]
        for r,c in pacific:
            mark(r,c,1)
        
        altlantic=[[R-1,c] for c in range(C)]+[[r,C-1] for r in range(R)]
        for r,c in altlantic:
            mark(r,c,2)
        
        for r in range(R):
            for c in range(C):
                if visited[r][c]==3:
                    ret.append([r,c])
        return ret
    



# @lc code=end

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().pacificAtlantic(heights))
heights = [[2,1],[1,2]]
print(Solution().pacificAtlantic(heights))