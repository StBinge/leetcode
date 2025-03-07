#
# @lc app=leetcode.cn id=2741 lang=python3
# @lcpr version=30204
#
# [2741] 特别的排列
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        N=len(nums)
        Mask=(1<<N)-1
        mod=10**9+7

        adj=defaultdict(list)
        nums.sort()
        for i in range(N):
            for j in range(i+1,N):
                if nums[j]%nums[i]==0:
                    adj[j].append(i)
                    adj[i].append(j)
        
        @cache
        def dfs(pre,mask):
            if mask==Mask:
                return 1
            ret=0
            for nxt in adj[pre]:
                if mask & 1<<nxt:
                    continue
                ret+=dfs(nxt,mask|(1<<nxt))
            return ret%mod

        return sum(dfs(i,1<<i) for i in range(N))%mod

# @lc code=end
assert Solution().specialPerm([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192])==178290591
assert Solution().specialPerm([1,4,3])==2
assert Solution().specialPerm([2,3,6])==2


#
# @lcpr case=start
# [2,3,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,3]\n
# @lcpr case=end

#

