#
# @lc app=leetcode.cn id=1332 lang=python3
#
# [1332] 删除回文子序列
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        L=len(s)
        if L==1:
            return 1
        l,r=0,L-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                break
        else:
            return 1
        return 2
# @lc code=end
assert Solution().removePalindromeSub('baabb')==2
assert Solution().removePalindromeSub('abb')==2
assert Solution().removePalindromeSub('ababa')==1
