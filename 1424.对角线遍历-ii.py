#
# @lc app=leetcode.cn id=1424 lang=python3
#
# [1424] 对角线遍历 II
#
from sbw import *
# @lc code=start
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ret=[]
        rows=len(nums)
        # for i,row in enumerate(nums):
        cols=max(len(row) for row in nums)
        buckets=[[] for _ in range(rows+cols-1)]
        for r in range(rows-1,-1,-1):
            row=nums[r]
            l=len(row)
            for c in range(cols):
                if c==l:
                    break
                buckets[r+c].append(nums[r][c])
        for bucket in buckets:
            ret.extend(bucket)
        return ret
        # for r in range(rows):
        #     cols=max(cols,len(nums[r]))
        #     for j in range(r+1):
        #         if j>=len(nums[r-j]):
        #             continue
        #         ret.append(nums[r-j][j])
        # for c in range(1,cols):
        #     for i in range(c,cols):
        #         if i>=len(nums[rows-i+c-1]):
        #             continue
        #         ret.append(nums[rows-i+c-1][i])
        # return ret
# @lc code=end
assert Solution().findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])==[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
assert Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])==[1,4,2,7,5,3,8,6,9]
assert Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])==[1,4,2,7,5,3,8,6,9]
