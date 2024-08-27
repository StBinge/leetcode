#
# @lc app=leetcode.cn id=2009 lang=python3
# @lcpr version=30204
#
# [2009] 使数组连续的最少操作数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N=len(nums)
        sorted_nums=sorted(set(nums))
        l=0
        ret=0
        for i,n in enumerate(sorted_nums):
            while n-sorted_nums[l]>=N:
                l+=1
            ret=max(ret,i-l+1)
        return N-ret
# @lc code=end
assert Solution().minOperations([41,33,29,33,35,26,47,24,18,28])==5
assert Solution().minOperations([1,10,100,1000])==3
assert Solution().minOperations([1,2,3,5,6])==1
assert Solution().minOperations([4,2,5,3])==0


#
# @lcpr case=start
# [4,2,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,10,100,1000]\n
# @lcpr case=end

#

