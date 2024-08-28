#
# @lc app=leetcode.cn id=690 lang=python3
# @lcpr version=30204
#
# [690] 员工的重要性
#

from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        em = {}
        for item in employees:
            em[item.id] = [item.importance, item.subordinates]

        def dfs(eid):
            p, childs = em[eid]
            for c in childs:
                p += dfs(c)
            return p

        ret = dfs(id)
        return ret


# @lc code=end
assert Solution().getImportance(employees=[[1, 2, [5]], [5, -3, []]], id=5) == -3
assert (
    Solution().getImportance(employees=[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], id=1)
    == 11
)


#
# @lcpr case=start
# [[1,5,[2,3]],[2,3,[]],[3,3,[]]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,[5]],[5,-3,[]]]\n5\n
# @lcpr case=end

#
