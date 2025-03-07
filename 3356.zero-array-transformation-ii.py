#
# @lc app=leetcode.cn id=3356 lang=python3
# @lcpr version=30204
#
# [3356] 零数组变换 II
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N=len(nums)
        difs=[0]*(N+1)
        qidx=0
        cur=0
        M=len(queries)
        for i in range(N):
            d,n=difs[i],nums[i]
            cur+=d
            while cur<n and qidx<M:
                l,r,val=queries[qidx]
                difs[l]+=val
                difs[r+1]-=val
                if l<=i<=r:
                    cur+=val   
                qidx+=1             
            if cur<n:
                return -1
        return qidx
        
# @lc code=end
assert Solution().minZeroArray([8,4],[[0,1,5],[1,1,5],[1,1,3],[1,1,4],[0,0,3],[1,1,4],[0,1,2],[1,1,3],[1,1,1]])==5
assert Solution().minZeroArray([5],[[0,0,5],[0,0,1],[0,0,3],[0,0,2]])==1
assert Solution().minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]])==-1
assert Solution().minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]])==2


#
# @lcpr case=start
# [2,0,2]\n[[0,2,1],[0,2,1],[1,1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n[[1,3,2],[0,2,1]]\n
# @lcpr case=end

#

