#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#
from typing import List
# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        R,C=len(matrix),len(matrix[0])
        left=matrix[0][0]
        right=matrix[-1][-1]+1
        while left<right:
            mid=(left+right)//2
            cnt=0
            c=0
            for r in range(R-1,-1,-1):
                while c<C and matrix[r][c]<=mid:
                    c+=1
                cnt+=c
            if cnt>=k:
                right=mid
            else:
                left=mid+1
        return left

# @lc code=end
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
assert Solution().kthSmallest(matrix,k)==13

matrix = [[-5]]
k = 1
assert Solution().kthSmallest(matrix,k)==-5
