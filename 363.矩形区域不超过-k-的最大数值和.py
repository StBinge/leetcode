#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#
from typing import List

# @lc code=start
class SortedSet:
    def __init__(self) -> None:
        self.array=[]
        self.set=set()
    
    def add(self,value):
        if value in self.set:
            return
        self.set.add(value)
        self.array.insert(self.bisect_right(value),value)

    def bisect_right(self,value):
        left,right=0,len(self.array)
        while left<right:
            mid=(left+right)//2
            x=self.array[mid]
            if x<value:
                left=mid+1
            else:
                right=mid
        return left
    
    def bisect_left(self,value):
        left,right=0,len(self.array)
        x=0
        while left<right:
            mid=(left+right)//2
            x=self.array[mid]
            if x>value:
                right=mid
            else:
                left=mid+1
        return left-1
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R,C=len(matrix),len(matrix[0])
        col_sums=[[0]*C for _ in range(R+1)]
        for r in range(R):
            for c in range(C):
                col_sums[r+1][c]=matrix[r][c]+col_sums[r][c]

        ret=float('-inf')
        for top in range(R):
            sums=[0]*C
            for bottom in range(top,R):
                for c in range(C):
                    sums[c]=col_sums[bottom+1][c]-col_sums[top][c]

                ss=SortedSet()
                ss.add(0)
                total=0
                for col in sums:
                    total+=col
                    idx=ss.bisect_right(total-k)
                    if idx<len(ss.array):
                        ret=max(ret,total-ss.array[idx])
                        if ret==k:
                            return k
                    ss.add(total)
        return ret
# @lc code=end

matrix =[[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
k = 3
assert Solution().maxSumSubmatrix(matrix,k)==2


matrix =[[2,2,-1]]
k = 0
assert Solution().maxSumSubmatrix(matrix,k)==-1



matrix = [[1,0,1],[0,-2,3]]
k = 2
assert Solution().maxSumSubmatrix(matrix,k)==2
matrix = [[2,2,-1]]
k = 3
assert Solution().maxSumSubmatrix(matrix,k)==3
