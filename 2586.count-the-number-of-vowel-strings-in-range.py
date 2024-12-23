#
# @lc app=leetcode.cn id=2586 lang=python3
# @lcpr version=30204
#
# [2586] 统计范围内的元音字符串数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ret=0
        vows='aeiou'
        for word in words[left:right+1]:
            if word[0] in vows and word[-1] in vows:
                ret+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# ["are","amy","u"]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# ["hey","aeo","mu","ooo","artro"]\n1\n4\n
# @lcpr case=end

#

