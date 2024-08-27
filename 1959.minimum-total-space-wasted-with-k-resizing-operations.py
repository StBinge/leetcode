#
# @lc app=leetcode.cn id=1959 lang=python3
# @lcpr version=30204
#
# [1959] K 次调整数组大小浪费的最小总空间
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        k+=1
        N=len(nums)
        g=[[0]*N for _ in range(N)]
        for i in range(N):
            mx=tot=0
            for j in range(i,N):
                mx=max(mx,nums[j])
                tot+=nums[j]
                g[i][j]=mx*(j-i+1)-tot
        
        f=[[float('inf')]*(k+1) for _ in range(N+1)]
        f[0][0]=0
        for i in range(N):
            for j in range(1,min(i+1,k)+1):
                v=f[i+1][j]
                for ii in range(i,max(-1,j-2),-1):
                    v=min(v,f[ii][j-1]+g[ii][i])
                f[i+1][j]=v
        return f[-1][-1]
# @lc code=end
assert Solution().minSpaceWastedKResizing(nums = [10,20,15,30,20], k = 2)==15
assert Solution().minSpaceWastedKResizing(nums = [10,20,30], k = 1)==10
assert Solution().minSpaceWastedKResizing(nums = [10,20], k = 0)==10


#
# @lcpr case=start
# [10,20]\n0\n
# @lcpr case=end

# @lcpr case=start
# [10,20,30]\n1\n
# @lcpr case=end

# @lcpr case=start
# [10,20,15,30,20]\n2\n
# @lcpr case=end

#

