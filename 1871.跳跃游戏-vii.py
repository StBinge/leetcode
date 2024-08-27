#
# @lc app=leetcode.cn id=1871 lang=python3
#
# [1871] 跳跃游戏 VII
#


# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != "0":
            return False
        N = len(s)
        # positions=[i for i in range(N) if s[i]=='0']
        f = [False] * N
        f[0] = True
        p=[0]*N
        for i in range(minJump):
            p[i]=1
        for i in range(minJump, N):
            if s[i] == "1":
                p[i]=p[i-1]
                continue
            left=i-maxJump
            right=i-minJump
            cnt=p[right]-(p[left-1] if left>0 else 0)
            f[i]=cnt>0
            p[i]=f[i]+p[i-1]
        return f[-1]

# @lc code=end
assert Solution().canReach(s="01101110", minJump=2, maxJump=3) == False
assert Solution().canReach("011010", 2, 3)
