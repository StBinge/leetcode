#
# @lc app=leetcode.cn id=1163 lang=python3
#
# [1163] 按字典序排在最后的子串
#

# @lc code=start
class Solution:
    def lastSubstring(self, s: str) -> str:
        i,j,n=0,1,len(s)
        k=0
        while j+k<n:
            if s[i+k]==s[j+k]:
                k+=1
            elif s[i+k]>s[j+k]:
                j+=k+1
                k=0
            else:
                i=i+k+1
                j=max(j,i+1)
                k=0
        return s[i:]
# @lc code=end
assert Solution().lastSubstring('xbylisvborylklftlkcioajuxwdhahdgezvyjbgaznzayfwsaumeccpfwamfzmkinezzwobllyxktqeibfoupcpptncggrdqbkji')=='zzwobllyxktqeibfoupcpptncggrdqbkji'
assert Solution().lastSubstring('leetcode')=='tcode'
assert Solution().lastSubstring('abab')=='bab'
