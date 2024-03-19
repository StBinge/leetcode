#
# @lc app=leetcode.cn id=1328 lang=python3
#
# [1328] 破坏回文串
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        L=len(palindrome)
        if L==1:
            return ''
        for i in range(L//2):
            if palindrome[i]=='a':
                continue
            return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b'

# @lc code=end
assert Solution().breakPalindrome('aba')=='abb'
assert Solution().breakPalindrome('a')==''
assert Solution().breakPalindrome('abccba')=='aaccba'
