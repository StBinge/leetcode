#
# @lc app=leetcode.cn id=2563 lang=python3
# @lcpr version=30204
#
# [2563] 统计公平数对的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ret=0
        left=right=len(nums)-1
        for i,n in enumerate(nums):
            while right>=0 and nums[right]+n>upper:
                right-=1
            if right<=i:
                break
            while left>=0 and nums[left]+n>=lower:
                left-=1
            ret+=max(i,right)-max(i,left)
        return ret

# @lc code=end
assert Solution().countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)==1
assert Solution().countFairPairs([0,0,0,0,0,0],0,0)==15
assert Solution().countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)==6


#
# @lcpr case=start
# [0,1,7,4,4,5]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,7,9,2,5]\n11\n11\n
# @lcpr case=end

#

