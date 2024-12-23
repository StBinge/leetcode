#
# @lc app=leetcode.cn id=2730 lang=python3
# @lcpr version=30204
#
# [2730] 找到最长的半重复子字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        repeated=False
        left=0
        ret=0
        for right in range(1,len(s)):
            if s[right]!=s[right-1]:
                continue
            elif repeated==False:
                repeated=True
                continue
            ret=max(ret,right-left)
            while s[left]!=s[left+1]:
                left+=1
            left+=1
        return max(ret,len(s)-left)
# @lc code=end
assert Solution().longestSemiRepetitiveSubstring('1111111')==2
assert Solution().longestSemiRepetitiveSubstring('5794')==4
assert Solution().longestSemiRepetitiveSubstring('52233')==4


#
# @lcpr case=start
# "52233"\n
# @lcpr case=end

# @lcpr case=start
# "5494"\n
# @lcpr case=end

# @lcpr case=start
# "1111111"\n
# @lcpr case=end

#

