#
# @lc app=leetcode.cn id=1764 lang=python3
#
# [1764] 通过连接另一个数组的子数组得到一个数组
#
from sbw import *
# @lc code=start
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        def calc_next(p: str | list):
            N = len(p)
            next = [0] * N
            j = 0
            for i in range(1, N):
                while j and p[j] != p[i]:
                    j = next[j - 1]
                if p[j] == p[i]:
                    j += 1
                next[i] = j
            return next
        idx=0
        N=len(nums)
        for g in groups:
            next=calc_next(g)
            gid=0
            m=len(g)
            while idx<N:
                while gid and nums[idx]!=g[gid]:
                    gid=next[gid-1]
                if nums[idx]==g[gid]:
                    gid+=1
                idx+=1
                if gid==m:
                    break
            if gid<m:
                return False
        return True
# @lc code=end
assert Solution().canChoose([[1,2]],[1,3,2])==False
assert Solution().canChoose(groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7])==False

assert Solution().canChoose(groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2])==False
assert Solution().canChoose(groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0])
