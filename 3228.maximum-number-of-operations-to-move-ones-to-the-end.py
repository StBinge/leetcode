#
# @lc app=leetcode.cn id=3228 lang=python3
# @lcpr version=30204
#
# [3228] 将 1 移动到末尾的最大操作次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxOperations(self, s: str) -> int:
        ret=0
        ones=0
        for i,ch in enumerate(s):
            if ch=='1':
                ones+=1
            elif i>0 and s[i-1]=='1':
                ret+=ones
        return ret
# @lc code=end
assert Solution().maxOperations('1001101')==4


#
# @lcpr case=start
# "1001101"\n
# @lcpr case=end

# @lcpr case=start
# "00111"\n
# @lcpr case=end

#

