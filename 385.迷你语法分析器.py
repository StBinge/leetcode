#
# @lc app=leetcode.cn id=385 lang=python3
#
# [385] 迷你语法分析器
#
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0]!='[':
            return NestedInteger(int(s))
        stack:list[NestedInteger]=[]
        idx=0
        L=len(s)
        neg=False
        while idx<L:
            if s[idx]=='[':
                stack.append(NestedInteger())
                idx+=1
            elif s[idx]==']' and len(stack)>1:
                stack[-2].add(stack.pop())
                idx+=1
            elif s[idx]=='-':
                neg=True
                idx+=1
            elif s[idx].isnumeric():
                start=idx
                while s[idx].isnumeric():
                    idx+=1
                num=int(s[start:idx])
                if neg:
                    num=-num
                    neg=False
                stack[-1].add(NestedInteger(num))
            else:
                idx+=1
        return stack[-1]
# @lc code=end
r=Solution().deserialize('324')
r=Solution().deserialize("[123,[456,[789]]]")
pass

