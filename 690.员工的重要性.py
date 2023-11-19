#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#
from typing import List
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

# @lc code=start
"""
# Definition for Employee.
"""
# class Node:
#     def __init__(self,id,val) -> None:
#         self.id=id
#         self.val=val
#         self.nodes=[]
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        nodes={}
        for em in employees:
            nodes[em.id]=em
        
        ret=0
        queue=[id]
        while queue:
            idx=queue.pop()
            ret+=nodes[idx].importance
            queue.extend(nodes[idx].subordinates)
        return ret
    


# @lc code=end
assert Solution().getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)==11
