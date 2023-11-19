#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#
class NestedInteger:
   def __init__(self,item) -> None:
       self.item=item
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       return isinstance(self.item,int)

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       return self.item if self.isInteger() else None

   def getList(self) -> list['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       return self.item if not self.isInteger() else None

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        # self.source=nestedList
        self.stack=nestedList[::-1]
        # self.cur=None
    
    def next(self) -> int:
        return self.stack.pop().getInteger()

        

    
    def hasNext(self) -> bool:
        while self.stack and self.stack[-1].isInteger()==False:
            self.stack+=self.stack.pop().getList()[::-1]
        return self.stack
            
             


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

nested=[NestedInteger([])]
itor=NestedIterator(nested)
ret=[]
while itor.hasNext():
    ret.append(itor.next())

print(ret)

nested=[NestedInteger([[1,1],2,[1,1]])]
itor=NestedIterator(nested)
ret=[]
while itor.hasNext():
    ret.append(itor.next())

print(ret)

nested=[NestedInteger([1,[4,[6]]])]
itor=NestedIterator(nested)
ret=[]
while itor.hasNext():
    ret.append(itor.next())

print(ret)