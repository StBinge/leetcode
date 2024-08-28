#
# @lc app=leetcode.cn id=2063 lang=python3
# @lcpr version=30204
#
# [2063] 所有子字符串中的元音
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countVowels(self, word: str) -> int:
        ret=0
        N=len(word)
        for i,ch in enumerate(word):
            if ch not in 'aeiou':
                continue
            ret+=(i+1)*(N-i)
        return ret
# @lc code=end



#
# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "ltcd"\n
# @lcpr case=end

# @lcpr case=start
# "noosabasboosa"\n
# @lcpr case=end

#

