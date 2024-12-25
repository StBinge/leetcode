#
# @lc app=leetcode.cn id=2195 lang=python3
# @lcpr version=30204
#
# [2195] 向数组中追加 K 个整数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums=sorted(set(nums))
        for i,n in enumerate(nums):
            if i+k<n:
                return (i+k)*(1+i+k)//2 - sum(nums[:i])
        N=len(nums)
        return (1+N+k)*(N+k)//2 - sum(nums)


# @lc code=end
assert Solution().minimalKSum([96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84],35)==794
assert Solution().minimalKSum(nums = [5,6], k = 6)==25


#
# @lcpr case=start
# [1,4,25,10,25]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,6]\n6\n
# @lcpr case=end

#

