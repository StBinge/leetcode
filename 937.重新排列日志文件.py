#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#
from sbw import *
# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log:str):
            a,b=log.split(' ',1)
            return (0,b,a) if b[0].isalpha() else (1,)
        logs.sort(key=trans)
        return logs
# @lc code=end
logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
ret=["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
assert Solution().reorderLogFiles(logs)==ret

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
ret=["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
assert Solution().reorderLogFiles(logs)==ret