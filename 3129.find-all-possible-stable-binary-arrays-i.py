#
# @lc app=leetcode.cn id=3129 lang=python3
# @lcpr version=30204
#
# [3129] 找出所有稳定的二进制数组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod=10**9+7

        f0=[[0]*(one+1) for _ in range(zero+1)]
        f1=[[0]*(one+1) for _ in range(zero+1)]

        for i in range(min(limit,one)+1):
            f1[0][i]=1
        
        for i in range(min(limit,zero)+1):
            f0[i][0]=1
        
        for i in range(1,zero+1):
            for j in range(1,one+1):
                if i>limit:
                    f0[i][j]=f0[i-1][j]+f1[i-1][j]-f1[i-limit-1][j]
                else:
                    f0[i][j]=f0[i-1][j]+f1[i-1][j]
                f0[i][j]%=mod

                if j>limit:
                    f1[i][j]=f1[i][j-1]+f0[i][j-1]-f0[i][j-limit-1]
                else:
                    f1[i][j]=f0[i][j-1]+f1[i][j-1]
                f1[i][j]%=mod
        
        return (f0[i][j]+f1[i][j])%mod
            
    

# @lc code=end
assert Solution().numberOfStableArrays(59,55,97)==718534091
assert Solution().numberOfStableArrays(3,3,2)==14
assert Solution().numberOfStableArrays(1,1,2)==2
assert Solution().numberOfStableArrays(1,2,1)==1


#
# @lcpr case=start
# 1\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n2\n
# @lcpr case=end

#

