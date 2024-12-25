#
# @lc app=leetcode.cn id=3153 lang=python3
# @lcpr version=30204
#
# [3153] 所有数对中数位不同之和
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        N=len(nums)
        tot=N*(N-1)//2
        ret=0
        while nums[0]>0:                
            cnt=defaultdict(int)
            ret+=tot
            for i in range(N):
                x,d=divmod(nums[i],10)                
                ret-=cnt[d]
                cnt[d]+=1
                nums[i]=x

        return ret

# @lc code=end
assert Solution().sumDigitDifferences([13,23,12])==4


#
# @lcpr case=start
# [13,23,12]\n
# @lcpr case=end

# @lcpr case=start
# [10,10,10,10]\n
# @lcpr case=end

#

