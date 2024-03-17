#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ret=cnt=0
        vows='aeiou'
        for i in range(k):
            if s[i] in vows:
                cnt+=1
        ret=cnt
        for i in range(k,len(s)):
            if s[i] in vows:
                cnt+=1
            if s[i-k] in vows:
                cnt-=1
            ret=max(ret,cnt)
            if ret==k:
                return k
        return ret

# @lc code=end

assert Solution().maxVowels(s = "leetcode", k = 3)==2
assert Solution().maxVowels(s = "abciiidef", k = 3)==3