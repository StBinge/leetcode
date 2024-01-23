#
# @lc app=leetcode.cn id=1206 lang=python3
#
# [1206] 设计跳表
#

# @lc code=start
import random
class ListNode:
    def __init__(self,val) -> None:
        self.val=val
        # self.level=level
        self.next:'ListNode'=None
        self.down:'ListNode'=None
    

class Skiplist:
    Min=-1
    Max=10**9
    P=0.5
    MaxLevel=32
    def __init__(self):
        self.heads:list[ListNode]=[ListNode(self.Min)]
        self.heads[-1].next=ListNode(self.Max)
        for i in range(1,self.MaxLevel):
            head=ListNode(self.Min)
            head.next=ListNode(self.Max)
            head.down=self.heads[-1]
            self.heads.append(head)
        self.level=1
    
    def random_level(self):
        p,max_level=self.P,self.MaxLevel
        lv=1
        while random.random()<p and lv<max_level:
            lv+=1
        return lv

    def search(self, target: int) -> bool:
        pre_node=self.heads[self.level-1]
        while pre_node:
            while pre_node.next.val<target:
                pre_node=pre_node.next
            if pre_node.next.val==target:
                return True
            pre_node=pre_node.down
        return False

    def add(self, num: int) -> None:
        lv=self.random_level()
        self.level=max(lv,self.level)
        pre_node=self.heads[lv-1]
        up_node:ListNode=None
        while pre_node:
            while pre_node.next.val<num:
                pre_node=pre_node.next
            node=ListNode(num)
            if up_node:
                up_node.down=node
            up_node=node
            node.next=pre_node.next
            pre_node.next=node
            pre_node=pre_node.down

    def erase(self, num: int) -> bool:
        pre_node=self.heads[self.level-1]
        erased=False
        while pre_node:
            while pre_node.next.val<num:
                pre_node=pre_node.next
            if pre_node.next.val==num:
                pre_node.next=pre_node.next.next
                erased=True
            pre_node=pre_node.down
        while self.level>1 and self.heads[self.level-1].next.val==self.Max:
            self.level-=1
        return erased


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end
obj=Skiplist()
obj.add(1)
obj.add(2)
obj.add(3)
assert obj.search(0) ==False
obj.add(4)
assert obj.search(1) 
assert obj.erase(0)==False
assert obj.erase(1)
assert obj.search(1) ==False

