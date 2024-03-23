#
# @lc app=leetcode.cn id=1439 lang=python3
#
# [1439] 有序矩阵中的第 k 个最小数组和
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def smallest_pairs(nums1:list,nums2:list):
            h=[(nums1[0]+nums2[0],0,0)]
            ans=[]
            while h and len(ans)<k:
                _,i,j=heapq.heappop(h)
                ans.append(nums1[i]+nums2[j])
                if j==0 and i+1<len(nums1):
                    heapq.heappush(h,(nums1[i+1]+nums2[0],i+1,j))
                if j+1<len(nums2):
                    heapq.heappush(h,(nums1[i]+nums2[j+1],i,j+1))
            return ans

        a=mat[0][:k]
        for row in mat[1:]:
            a=smallest_pairs(a,row[:k])
        return a[-1]

# @lc code=end
assert Solution().kthSmallest(mat = [[1,1,10],[2,2,9]], k = 7)==12
assert Solution().kthSmallest(mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7)==9
assert Solution().kthSmallest(mat = [[1,3,11],[2,4,6]], k = 9)==17
assert Solution().kthSmallest(mat = [[1,3,11],[2,4,6]], k = 5)==7
