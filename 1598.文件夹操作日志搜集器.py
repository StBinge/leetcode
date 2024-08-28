#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#
from sbw import *


# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ret = 0
        for log in logs:
            if log=='./':
                continue
            elif log != "../":
                ret+=1
            elif ret:
                ret -=1
        return ret


# @lc code=end
assert Solution().minOperations(["d1/", "d2/", "../", "d21/", "./"]) == 2
