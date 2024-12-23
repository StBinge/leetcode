#
# @lc app=leetcode.cn id=3274 lang=python3
# @lcpr version=30204
#
# [3274] 检查棋盘方格颜色是否相同
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        r1,c1=coordinate1
        r2,c2=coordinate2
        return (ord(r1)+ord(r2))%2==(ord(c1)+ord(c2))%2

# @lc code=end
assert Solution().checkTwoChessboards('a1','h3')==False
assert Solution().checkTwoChessboards('a1','c3')


#
# @lcpr case=start
# "a1"\n"c3"\n
# @lcpr case=end

# @lcpr case=start
# "a1"\n"h3"\n
# @lcpr case=end

#

