#
# @lc app=leetcode.cn id=2602 lang=python3
# @lcpr version=30204
#
# [2602] 使数组元素全部相等的最少操作次数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        N=len(queries)
        sorted_qid=sorted(range(N),key=queries.__getitem__)
        nums.sort()
        ret=[0]*N
        left=0
        right=sum(nums)
        M=len(nums)
        idx=0
        for qid in sorted_qid:
            q=queries[qid]
            while idx<M and nums[idx]<=q:
                left+=nums[idx]
                right-=nums[idx]
                idx+=1
            cnt=idx*q - left + right- (M-idx)*q
            ret[qid]=cnt
        return ret
# @lc code=end
assert Solution().minOperations(nums = [2,9,6,3], queries = [10])==[20]
assert Solution().minOperations(nums = [3,1,6,8], queries = [1,5])==[14,10]


#
# @lcpr case=start
# [3,1,6,8]\n[1,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,9,6,3]\n[10]\n
# @lcpr case=end

#

