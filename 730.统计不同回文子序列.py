#
# @lc app=leetcode.cn id=730 lang=python3
#
# [730] 统计不同回文子序列
#

# @lc code=start
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD=10**9+7
        L=len(s)
        f=[[0]*L for _ in range(L)]
        next=[[L]*4 for _ in range(L)]
        prev=[[-1]*4 for _ in range(L)]
        pos=[-1]*4
        for i in range(L):
            for c in range(4):
                prev[i][c]=pos[c]
            pos[ord(s[i])-ord('a')]=i

        pos=[L]*4

        for i in range(L-1,-1,-1):
            for c in range(4):
                next[i][c]=pos[c]
            pos[ord(s[i])-ord('a')]=i

        for i in range(L):
            f[i][i]=1
        
        for sz in range(2,L+1):
            for i in range(L-sz+1):
                j=i+sz-1
                if s[i]==s[j]:
                    low=next[i][ord(s[i])-ord('a')]
                    high=prev[j][ord(s[j])-ord('a')]
                    if low>high:
                        f[i][j]=2+2*f[i+1][j-1]
                    elif low==high:
                        f[i][j]=2*f[i+1][j-1]+1
                    else:
                        f[i][j]=2*f[i+1][j-1]-f[low+1][high-1]
                else:
                    f[i][j]=f[i+1][j]+f[i][j-1]-f[i+1][j-1]
                f[i][j]%=MOD
        return f[0][-1]%MOD
# @lc code=end
assert Solution().countPalindromicSubsequences('bccb')==6
assert Solution().countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba')==104860361
