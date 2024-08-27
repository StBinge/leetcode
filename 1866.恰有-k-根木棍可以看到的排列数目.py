#
# @lc app=leetcode.cn id=1866 lang=python3
#
# [1866] 恰有 K 根木棍可以看到的排列数目
#


# @lc code=start
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        f0=[1]+[0]*k
        Mod=10**9+7
        f1=[0]*(k+1)
        for i in range(n):
            for j in range(1,k+1):
                f1[j]=(f0[j-1]+i*f0[j])%Mod
            f1[0]=0
            f0,f1=f1,f0
        return f0[-1]


# @lc code=end
assert Solution().rearrangeSticks(20,11) == 647427950
assert Solution().rearrangeSticks(5, 5) == 1
assert Solution().rearrangeSticks(3, 2) == 3
