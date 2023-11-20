#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有 K 个重复字符的最长子串
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k==1:
            return len(s)
        L=len(s)
        ret=0
        for t in range(1,26):
            total,less=0,0
            l,r=0,0
            cnt=[0]*26
            while r<L:
                idx=ord(s[r])-ord('a')
                cnt[idx]+=1
                if cnt[idx]==1:
                    less+=1
                    total+=1
                elif cnt[idx]==k:
                    less-=1

                while total>t:
                    idx=ord(s[l])-ord('a')
                    cnt[idx]-=1
                    if cnt[idx]==0:
                        total-=1
                        less-=1
                    elif cnt[idx]==k-1:
                        less+=1
                    l+=1
                if less==0:
                    ret=max(ret,r-l+1)
                r+=1
        return ret

           


                
# @lc code=end
assert Solution().longestSubstring('bbaaacbd',3)==3
assert Solution().longestSubstring('ababacb',3)==0
assert Solution().longestSubstring('aaabb',3)==3
assert Solution().longestSubstring('ababbc',2)==5
