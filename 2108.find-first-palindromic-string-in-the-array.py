#
# @lc app=leetcode.cn id=2108 lang=python3
# @lcpr version=30204
#
# [2108] 找出数组中的第一个回文字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left,right=0,len(word)-1
            while left<right:
                if word[left]!=word[right]:
                    break
                left+=1
                right-=1
            else:
                return word
        return ''
# @lc code=end
assert Solution().firstPalindrome()


#
# @lcpr case=start
# ["abc","car","ada","racecar","cool"]\n
# @lcpr case=end

# @lcpr case=start
# ["notapalindrome","racecar"]\n
# @lcpr case=end

# @lcpr case=start
# ["def","ghi"]\n
# @lcpr case=end

#

