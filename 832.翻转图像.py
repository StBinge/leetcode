#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#
from typing import List
# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        C=len(image[0])
        for row in image:
            l,r=0,C-1
            while l<r:
                if row[l]==row[r]:
                    row[l]^=1
                    row[r]=row[l]
                l+=1
                r-=1
            if l==r:
                row[l]^=1
        return image
# @lc code=end

