#
# @lc app=leetcode.cn id=935 lang=python3
#
# [935] 骑士拨号器
#

# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        jumps=[
            [4,6],#0
            [6,8],#1
            [7,9],#2
            [4,8],#3
            [3,9,0],#4
            [],#5
            [1,7,0],#6
            [2,6],#7
            [1,3],#8
            [2,4],#9

        ]
        f1=[1]*10
        Mod=10**9+7
        for i in range(n-1):
            f2=[0]*10
            for j in range(10):
                for nxt in jumps[j]:
                    f2[nxt]+=f1[j]
                    f2[nxt]%=Mod
            f1=f2
        return sum(f1)%(10**9+7)
# @lc code=end
assert Solution().knightDialer(3131)==136006598
assert Solution().knightDialer(2)==20

assert Solution().knightDialer(1)==10
