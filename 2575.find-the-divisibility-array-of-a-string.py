#
# @lc app=leetcode.cn id=2575 lang=python3
# @lcpr version=30204
#
# [2575] 找出字符串的可整除数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ret=[0]*len(word)
        pre=0
        for i,ch in enumerate(word):
            pre=((pre*10)+int(ch))%m
            if pre==0:
                ret[i]=1
        return ret
# @lc code=end



#
# @lcpr case=start
# "998244353"\n3\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n10\n
# @lcpr case=end

#

