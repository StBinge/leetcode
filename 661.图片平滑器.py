#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
from typing import List
# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R,C=len(img),len(img[0])
        ret=[[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                total=0
                cnt=0
                for x in [-1,0,1]:
                    rr=r+x
                    if rr<0 or rr>=R:
                        continue
                    for y in [-1,0,1]:
                        cc=c+y
                        if cc<0 or cc>=C:
                            continue
                        total+=img[rr][cc]
                        cnt+=1
                avg=total//cnt
                ret[r][c]=avg
        return ret

# @lc code=end  

