#
# @lc app=leetcode.cn id=2697 lang=python3
# @lcpr version=30204
#
# [2697] 字典序最小回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        left,right=0,len(s)-1
        while left<right:
            l,r=s[left],s[right]
            if l>r:
                s[left]=r
            elif l<r:
                s[right]=l
            left+=1
            right-=1
        return ''.join(s)

# @lc code=end



#
# @lcpr case=start
# "egcfe"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n
# @lcpr case=end

# @lcpr case=start
# "seven"\n
# @lcpr case=end

#

