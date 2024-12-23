#
# @lc app=leetcode.cn id=2344 lang=python3
# @lcpr version=30204
#
# [2344] 使数组可以被整除的最少删除次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        d=math.gcd(*numsDivide)
        mi=min([n for n in nums if d%n==0],default=0)
        return -1 if mi==0 else sum(n<mi for n in nums)

        

# @lc code=end
assert Solution().minOperations([3,2,6,2,35,5,35,2,5,8,7,3,4],[105,70,70,175,105,105,105])==6
assert Solution().minOperations([4,3,6],[8,2,6,10])==-1


#
# @lcpr case=start
# [2,3,2,4,3]\n[9,6,9,3,15]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,6]\n[8,2,6,10]\n
# @lcpr case=end

#

