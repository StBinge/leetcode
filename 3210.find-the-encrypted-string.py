#
# @lc app=leetcode.cn id=3210 lang=python3
# @lcpr version=30204
#
# [3210] 找出加密后的字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ret=[]
        N=len(s)
        for i in range(N):
            ret.append(s[(i+k)%N])
        return ''.join(ret)
# @lc code=end
assert Solution().getEncryptedString('dart',3)=='tdar'


#
# @lcpr case=start
# "dart"\n3\n
# @lcpr case=end

# @lcpr case=start
# "aaa"\n1\n
# @lcpr case=end

#

