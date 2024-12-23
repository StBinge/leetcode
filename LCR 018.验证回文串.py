#
# @lc app=leetcode.cn id=LCR 018 lang=python3
# @lcpr version=30204
#
# [LCR 018] 验证回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while left<right:
            while left<right and s[left].isalnum()==False:
                left+=1
            while left<right and s[right].isalnum()==False:
                right-=1
            if left==right:
                break
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

#

