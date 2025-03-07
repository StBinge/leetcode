#
# @lc app=leetcode.cn id=3362 lang=python3
# @lcpr version=30204
#
# [3362] 零数组变换 III
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N=len(nums)
        M=len(queries)
        queries.sort(key=lambda x:[x[0],-x[1]])
        qidx=0
        difs=[0]*(N+1)
        ret=0
        cur=0
        for i,n in enumerate(nums):
            cur+=difs[i]
            while cur<n and qidx<M and queries[qidx][0]<=i:
                if queries[qidx][1]<i:
                    ret+=1
                    qidx+=1
                    continue
                else:
                    cur+=1
                    difs[queries[qidx][1]+1]-=1
                    qidx+=1
            if cur<n:
                return -1
        return ret+M-qidx


# @lc code=end

assert Solution().maxRemoval([0,0,1,1,0],[[3,4],[0,2],[2,3]])==2
assert Solution().maxRemoval(nums = [1,2,3,4], queries = [[0,3]])==-1
assert Solution().maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]])==2
assert Solution().maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]])==1

#
# @lcpr case=start
# [2,0,2]\n[[0,2],[0,2],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n[[1,3],[0,2],[1,3],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n[[0,3]]\n
# @lcpr case=end

#

