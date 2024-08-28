#
# @lc app=leetcode.cn id=1691 lang=python3
#
# [1691] 堆叠长方体的最大高度
#
from sbw import *
# @lc code=start
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cub in cuboids:
            cub.sort(reverse=True)
        #[h,w,l]
        cuboids.sort()

        def check(cub1,cub2):
            return cub1[1]<=cub2[1] and cub1[2]<=cub2[2]
        N=len(cuboids)
        @cache
        def dfs(top,idx):
            if idx==N:
                return 0
            height=dfs(top,idx+1)
            if top==-1 or check(cuboids[top],cuboids[idx]):
                height=max(height,cuboids[idx][0]+dfs(idx,idx+1))
            return height
        return dfs(-1,0)
# @lc code=end
assert Solution().maxHeight(cuboids = [[50,45,20],[95,37,53],[45,23,12]])==190
