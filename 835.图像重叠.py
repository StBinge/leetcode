#
# @lc app=leetcode.cn id=835 lang=python3
#
# [835] 图像重叠
#
from typing import List
# @lc code=start
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        counter={}
        for r1,row1 in enumerate(img1):
            for c1,v1 in enumerate(row1):
                if v1==0:
                    continue
                for r2,row2 in enumerate(img2):
                    for c2,v2 in enumerate(row2):
                        if v2==0:
                            continue
                        dif=(r2-r1,c2-c1)
                        counter[dif]=counter.get(dif,0)+1
        return max(counter.values(),default=0)
# @lc code=end
img1 = [[1,1,0],[0,1,0],[0,1,0]]
img2 = [[0,0,0],[0,1,1],[0,0,1]]
ret=3
assert Solution().largestOverlap(img1,img2)==ret

img1 = [[1]]
img2 = [[1]]
ret=1
assert Solution().largestOverlap(img1,img2)==ret
