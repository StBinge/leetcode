#
# @lc app=leetcode.cn id=1738 lang=python3
#
# [1738] 找出第 K 大的异或坐标值
#
from sbw import *
# @lc code=start
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        R,C=len(matrix),len(matrix[0])
        # xors=[[0]*(C+1) for _ in range(R+1)]
        xors=[0]*((R+1)*(C+1))
        def get_idx(r,c):
            return r*(C+1)+c
        for i in range(R):
            for j in range(C):
                xors[get_idx(i+1,j+1)]=xors[get_idx(i+1,j)]^xors[get_idx(i,j+1)]^xors[get_idx(i,j)]^matrix[i][j]
        
        k-=1
        def qsort(left,right):
            if left==right:
                return xors[left]
            pivot=randint(left,right)
            xors[pivot],xors[right]=xors[right],xors[pivot]
            sepl=sepr=left-1
            for i in range(left,right+1):
                if xors[i]>xors[right]:
                    sepr+=1
                    if sepr!=i:
                        xors[sepr],xors[i]=xors[i],xors[sepr]
                    sepl+=1
                    if sepl != sepr:
                        xors[sepl],xors[sepr]=xors[sepr],xors[sepl]
                elif xors[i]==xors[right]:
                    sepr+=1
                    if sepr!=i:
                        xors[sepr],xors[i]=xors[i],xors[sepr]
            if sepl<k<=sepr:
                return xors[k]
            elif sepl>=k:
                return qsort(left,sepl)
            else:
                return qsort(sepr,right)

        return qsort(0,len(xors)-1)
# @lc code=end
assert Solution().kthLargestValue([[8,10,5,8,5,7,6,0,1,4,10,6,4,3,6,8,7,9,4,2]],2)==14
assert Solution().kthLargestValue(matrix = [[5,2],[1,6]], k = 4)==0
assert Solution().kthLargestValue(matrix = [[5,2],[1,6]], k = 3)==4
assert Solution().kthLargestValue(matrix = [[5,2],[1,6]], k = 1)==7
