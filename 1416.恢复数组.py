#
# @lc app=leetcode.cn id=1416 lang=python3
#
# [1416] 恢复数组
#

# @lc code=start
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        L=len(s)
        f=[0]*(L+1)
        f[-1]=1
        # if s[-1]!='0' and int(s[-1])<=k:
        #     f[-2]=1
        Mod=10**9+7
        for i in range(L-1,-1,-1):
            if s[i]=='0':
                continue
            # n=int(s[i])
            # f[i]=1
            n=0
            for j in range(i,L):
                n=n*10+int(s[j])
                if n<=k:
                    f[i]+=f[j+1]
                else:
                    break
            f[i]%=Mod
        return f[0]
# @lc code=end
assert Solution().numberOfArrays(s = "1234567890", k = 90)==34
assert Solution().numberOfArrays(s = "2020", k = 30)==1
assert Solution().numberOfArrays(s = "1317", k = 2000)==8
assert Solution().numberOfArrays('1000',10000)==1
assert Solution().numberOfArrays(s = "1000", k = 10)==0
