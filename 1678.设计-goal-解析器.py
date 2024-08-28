#
# @lc app=leetcode.cn id=1678 lang=python3
#
# [1678] 设计 Goal 解析器
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        ret=[]
        idx=0
        N=len(command)
        while idx<N:
            c=command[idx]
            if c=='G':
                ret.append('G')
                idx+=1
            elif c=='(':
                if command[idx+1]==')':
                    ret.append('o')
                    idx+=2
                else:
                    ret.append('al')
                    idx+=4
        return ''.join(ret)
# @lc code=end
assert Solution().interpret("G()()()()(al)")=="Gooooal"
assert Solution().interpret("G()(al)")=='Goal'
