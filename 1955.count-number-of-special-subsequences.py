#
# @lc app=leetcode.cn id=1955 lang=python3
# @lcpr version=30204
#
# [1955] 统计特殊子序列的数目
#

from sbw import *
# @lcpr-templ_ate-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        Mods=10**9+7
        f1=f2=0
        cnt0=0
        for n in nums:
            if n==0:
                cnt0+=1
                continue
            elif not cnt0:
                continue

            if n==1:
                f0=(1<<cnt0)-1
                f1=(f0+(f1<<1))%Mods

            else:
                f2=(f1+(f2<<1))%Mods

        return f2

# @lc code=end
assert Solution().countSpecialSubsequences([0,1,2,0,1,2])==7
assert Solution().countSpecialSubsequences([2,2,0,0])==0
assert Solution().countSpecialSubsequences([0,1,2,2])==3


#
# @lcpr case=start
# [0,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,0,1,2]\n
# @lcpr case=end

#

