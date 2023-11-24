#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if n==1:
            return 1
        # f=[[0]*(k+1) for _ in range(n+1)]
        f=[0]*(k+1)
        for K in range(1,k+1):
            f[1][K]=1

        for m in range(2,n+1):
            for K in range(1,k+1):
                f[m][K]=f[m-1][K]+f[m-1][K-1]+1
            if f[m][k]>=n:
                return m
# @lc code=end
assert Solution().superEggDrop(3,14)==4
assert Solution().superEggDrop(2,2)==2
assert Solution().superEggDrop(2,6)==3
assert Solution().superEggDrop(1,2)==2
