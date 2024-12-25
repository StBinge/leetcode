#
# @lc app=leetcode.cn id=3289 lang=python3
# @lcpr version=30204
#
# [3289] 数字小镇中的捣蛋鬼
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        N=len(nums)
        for i in range(N):
            nums[i]+=1
        for n in nums:
            n=abs(n)
            nums[n-1]=-nums[n-1]
        ret=[]
        for i in range(len(nums)-2):
            if nums[i]>0:
                ret.append(i)
        return ret
# @lc code=end
assert sorted(Solution().getSneakyNumbers([0,3,2,1,3,2]))==[2,3]
assert sorted(Solution().getSneakyNumbers([0,1,1,0]))==[0,1]


#
# @lcpr case=start
# [0,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,2,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [7,1,5,4,3,4,6,0,9,5,8,2]\n
# @lcpr case=end

#

