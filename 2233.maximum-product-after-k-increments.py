#
# @lc app=leetcode.cn id=2233 lang=python3
# @lcpr version=30204
#
# [2233] K 次增加后的最大乘积
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre_cnt=0
        pre=nums[0]
        mod=10**9+7
        for i,n in enumerate(nums):
            if n==pre:
                continue
            dif=n-pre
            if dif*i<=k:
                pre=n
                k-=dif*i
            else:
                add,m=divmod(k,i)
                pre_mul= pow(pre+add,i-m,mod)*pow(pre+add+1,m,mod)%mod
                for n in nums[i:]:
                    pre_mul=pre_mul*n%mod
                return pre_mul
        add,m=divmod(k,len(nums))
        return pow(nums[-1]+add,len(nums)-m,mod)*pow(nums[-1]+add+1,m,mod)%mod
# @lc code=end



#
# @lcpr case=start
# [0,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [6,3,3,2]\n2\n
# @lcpr case=end

#

