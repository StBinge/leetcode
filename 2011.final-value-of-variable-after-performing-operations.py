#
# @lc app=leetcode.cn id=2011 lang=python3
# @lcpr version=30204
#
# [2011] 执行操作后的变量值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ret=0
        for op in operations:
            if op[0]=='+' or op[-1]=='+':
                ret+=1
            else:
                ret-=1
        return ret
# @lc code=end



#
# @lcpr case=start
# ["--X","X++","X++"]\n
# @lcpr case=end

# @lcpr case=start
# ["++X","++X","X++"]\n
# @lcpr case=end

# @lcpr case=start
# ["X++","++X","--X","X--"]\n
# @lcpr case=end

#

