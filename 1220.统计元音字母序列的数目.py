#
# @lc app=leetcode.cn id=1220 lang=python3
#
# [1220] 统计元音字母序列的数目
#

# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        Mod=10**9+7
        # 0 1 2 3 4
        # a e i o u
        # f=[[1]*5 for _ in range(n)]
        a=e=i=o=u=1
        for _ in range(1,n):
            a,e,i,o,u=e+i+u,a+i,e+o,i,o+i
        return (a+e+i+o+u)%Mod
# @lc code=end
assert Solution().countVowelPermutation(5)==68
assert Solution().countVowelPermutation(2)==10
assert Solution().countVowelPermutation(1)==5
