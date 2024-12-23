#
# @lc app=leetcode.cn id=2696 lang=python3
# @lcpr version=30204
#
# [2696] 删除子串后的字符串最小长度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        ret=[]
        for ch in s:
            if ret and ((ch=='B' and ret[-1]=='A') or ch=='D' and ret[-1]=='C'):
                ret.pop()
                continue
            ret.append(ch)
        return len(ret)
# @lc code=end



#
# @lcpr case=start
# "ABFCACDB"\n
# @lcpr case=end

# @lcpr case=start
# "ACBBD"\n
# @lcpr case=end

#

