#
# @lc app=leetcode.cn id=1807 lang=python3
#
# [1807] 替换字符串中的括号内容
#
from sbw import *
# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge=dict(knowledge)
        ret=[]
        left=0
        for right in range(len(s)):
            if s[right]=='(':
                ret.append(s[left:right])
                left=right+1
            elif s[right]==')':
                v=knowledge.get(s[left:right],'?')
                ret.append(v)
                left=right+1
        ret.append(s[left:])
        return ''.join(ret)
# @lc code=end
assert Solution().evaluate(s = "hi(name)", knowledge = [["a","b"]])=="hi?"
assert Solution().evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]])=="bobistwoyearsold"
