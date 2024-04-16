#
# @lc app=leetcode.cn id=3030 lang=python3
#
# [3030] 找出网格的区域平均强度
#
from sbw import *
# @lc code=start
class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        R,C=len(image),len(image[0])
        # inf=float('-inf')
        ret=[[0]*C for _ in range(R)]
        cnt=[[0]*C for _ in range(R)]
        for r in range(2,R):
            for c in range(2,C):
                valid=True
                # check vert
                for cc in range(c-2,c+1):
                    if abs(image[r][cc]-image[r-1][cc])>threshold or abs(image[r-1][cc]-image[r-2][cc])>threshold:
                        valid=False
                        break
                if not valid:
                    continue
                # check hori
                for rr in range(r-2,r+1):
                    if abs(image[rr][c]-image[rr][c-1])>threshold or abs(image[rr][c-1]-image[rr][c-2])>threshold:
                        valid=False
                        break
                if not valid:
                    continue

                avg=sum(image[rr][cc] for rr in range(r-2,r+1) for cc in range(c-2,c+1))//9
                
                for rr in range(r-2,r+1):
                    for cc in range(c-2,c+1):
                        ret[rr][cc]+=avg
                        cnt[rr][cc]+=1
        for r in range(R):
            for c in range(C):
                if cnt[r][c]:
                    ret[r][c]=int(ret[r][c]//cnt[r][c])
                else:
                    ret[r][c]=image[r][c]
        return ret
 

# @lc code=end
assert Solution().resultGrid([[1,18,10,4],[9,4,7,6],[12,6,5,9]],13)==[[1,18,10,4],[9,4,7,6],[12,6,5,9]]
assert Solution().resultGrid([[1,14,9,2],[10,16,13,8],[7,11,12,4]],13)==[[10,9,9,9],[10,9,9,9],[10,9,9,9]]
assert Solution().resultGrid([[5,6,7,10],[8,9,10,10],[11,12,13,10]],3)==[[9,9,9,9],[9,9,9,9],[9,9,9,9]]
assert Solution().resultGrid(image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12)==[[25,25,25],[27,27,27],[27,27,27],[30,30,30]]
assert Solution().resultGrid(image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3)==[[9,9,9,9],[9,9,9,9],[9,9,9,9]]
