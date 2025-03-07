#
# @lc app=leetcode.cn id=3325 lang=python3
# @lcpr version=30204
#
# [3325] 字符至少出现 K 次的子字符串 I
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt=[0]*26
        left=0
        ret=0
        for ch in s:
            code=ord(ch)-97
            cnt[code]+=1
            if cnt[code]>=k:
                while s[left]!=ch:
                    cnt[ord(s[left])-97]-=1
                    left+=1
                left+=1
                cnt[code]-=1
            ret+=left
        return ret
# @lc code=end
assert Solution().numberOfSubstrings("biikmbqb",2)==16
assert Solution().numberOfSubstrings( s = "abcde", k = 1)==15
assert Solution().numberOfSubstrings(s = "abacb", k = 2)==4


#
# @lcpr case=start
# "abacb"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n1\n
# @lcpr case=end

#

