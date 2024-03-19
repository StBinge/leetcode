#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        cnt=[0]*3
        orda=ord('a')
        tot=0
        ret=0
        for r in range(len(s)):
            ch=s[r]
            idx=ord(ch)-orda
            cnt[idx]+=1
            if cnt[idx]==1:
                tot+=1
            while tot==3:
                ch=s[l]
                idx=ord(ch)-orda
                cnt[idx]-=1
                if cnt[idx]==0:
                    tot-=1
                l+=1
            ret+=l
        return ret
# @lc code=end
assert Solution().numberOfSubstrings('abc')==1
assert Solution().numberOfSubstrings('aaacb')==3
assert Solution().numberOfSubstrings('abcabc')==10
