#
# @lc app=leetcode.cn id=3216 lang=python3
# @lcpr version=30204
#
# [3216] 交换后字典序最小的字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getSmallestString(self, s: str) -> str:
        ss=list(s)
        for i in range(1,len(s)):
            if s[i-1]>s[i] and int(s[i-1])%2==int(s[i])%2:
                ss[i-1],ss[i]=ss[i],ss[i-1]
                break
        else:
            return s
        return ''.join(ss)
# @lc code=end



#
# @lcpr case=start
# "45320"\n
# @lcpr case=end

# @lcpr case=start
# "001"\n
# @lcpr case=end

#

