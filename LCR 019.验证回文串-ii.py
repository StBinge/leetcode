#
# @lc app=leetcode.cn id=LCR 019 lang=python3
# @lcpr version=30204
#
# [LCR 019] 验证回文串 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while left<right and s[left]==s[right]:
            left+=1
            right-=1
        
        if left==right:
            return True
        s1=s[left+1:right+1]
        if s1==s1[::-1]:
            return True
        s2=s[left:right]
        return s2==s2[::-1]
            
# @lc code=end

assert Solution().validPalindrome('cbbcc')

#
# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "abca"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

