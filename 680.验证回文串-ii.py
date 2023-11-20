#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文串 II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        def valid(left,right,skip=False):
            while left<=right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                    continue
                if skip:
                    return False
                return valid(left+1,right,True) or valid(left,right-1,True)
            return True
        return valid(left,right)
# @lc code=end

assert Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
assert Solution().validPalindrome('abc')==False
assert Solution().validPalindrome('aba')
assert Solution().validPalindrome('abca')
