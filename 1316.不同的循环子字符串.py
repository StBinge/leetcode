#
# @lc app=leetcode.cn id=1316 lang=python3
#
# [1316] 不同的循环子字符串
#

# @lc code=start
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        L=len(text)
        hashs=[0]*(L+1)
        mul=[0]*(L+1)
        mul[0]=1
        Mod=10**9+7
        k=31
        orda=ord('a')
        for i,c in enumerate(text):
            hashs[i+1]=(hashs[i]*k+ord(c)-orda)%Mod
            mul[i+1]=(mul[i]*k)%Mod
        
        def get_hash(l,r):
            return (hashs[r+1]-hashs[l]*(mul[r-l+1])+Mod)%Mod
        
        seen=set()
        for span in range(2,L+1,2):
            for i in range(L-span+1):
                j=i+span-1
                mid=i+span//2-1
                left=get_hash(i,mid)
                right=get_hash(mid+1,j)
                if left==right:
                    seen.add(text[i:j+1])
        return len(seen)
# @lc code=end

assert Solution().distinctEchoSubstrings('abcabcabc')==3