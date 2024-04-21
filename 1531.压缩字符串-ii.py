#
# @lc app=leetcode.cn id=1531 lang=python3
#
# [1531] 压缩字符串 II
#
from sbw import *
# @lc code=start
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def cost(cnt):
            if cnt==1:
                return 1
            elif cnt<10:
                return 2
            elif cnt<100:
                return 3
            return 4
        N=len(s)
        T=N-k
        f=[[100]*(T+1) for _ in range(N+1)]
        f[-1][-1]=0
        for i in range(N-1,-1,-1):
            for j in range(T+1):
                same=0
                for i0 in range(i,N):
                    same+=s[i]==s[i0]
                    if same + j>T:
                        break
                    f[i][j]=min(f[i][j],f[i0+1][j+same]+cost(same))
                f[i][j]=min(f[i][j],f[i+1][j])
        return f[0][0]

        


# @lc code=end
assert Solution().getLengthOfOptimalCompression(s = "abcdefghijklmnopqrstuvwxyz", k = 16)==10
assert Solution().getLengthOfOptimalCompression(s = "abc", k = 2)==1
assert Solution().getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0)==3
assert Solution().getLengthOfOptimalCompression(s = "aabbaa", k = 2)==2
assert Solution().getLengthOfOptimalCompression(s = "aaabcccd", k = 2)==4
