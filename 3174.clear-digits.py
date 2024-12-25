#
# @lc app=leetcode.cn id=3174 lang=python3
# @lcpr version=30204
#
# [3174] 清除数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def clearDigits(self, s: str) -> str:
        ret=[]
        rm=0
        for ch in reversed(s):
            if ch.isnumeric():
                rm+=1
            elif rm:
                rm-=1
            else:
                ret.append(ch)
        return ''.join(reversed(ret))
# @lc code=end



#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "cb34"\n
# @lcpr case=end

#

