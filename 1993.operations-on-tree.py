#
# @lc app=leetcode.cn id=1993 lang=python3
# @lcpr version=30204
#
# [1993] 树上的操作
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class LockingTree:

    def __init__(self, parent: List[int]):
        n=len(parent)
        self.parent=parent
        self.childs=[[] for _ in range(n)]
        for i in range(1,n):
            self.childs[parent[i]].append(i)
        self.locker=[-1]*n
        self.locked_childs=[0]*n

    def lock(self, num: int, user: int) -> bool:
        if self.locker[num]!=-1:
            return False
        self.locker[num]=user
        p=self.parent[num]
        while p!=-1:
            self.locked_childs[p]+=1
            p=self.parent[p]
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locker[num]!=user:
            return False
        self.locker[num]=-1
        p=self.parent[num]
        while p!=-1:
            self.locked_childs[p]-=1
            p=self.parent[p]
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locker[num]!=-1 or self.locked_childs[num]==0:
            return False
        p=self.parent[num]
        while p!=-1:
            if self.locker[p]!=-1:
                return False
            p=self.parent[p]

        q=[num]
        while q:
            cur=q.pop()
            self.locker[cur]=-1
            if self.locked_childs[cur]==0:
                continue
            self.locked_childs[cur]=0
            q.extend(self.childs[cur])
        self.lock(num,user)
        return True

        



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
# @lc code=end
lockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])#
assert lockingTree.lock(2, 2)
assert not lockingTree.unlock(2, 3)
assert lockingTree.unlock(2, 2)
assert lockingTree.lock(4, 5)
assert lockingTree.upgrade(0, 1)
assert not lockingTree.lock(0, 1)


#
# @lcpr case=start
# ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"][[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]\n
# @lcpr case=end

#

