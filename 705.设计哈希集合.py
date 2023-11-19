#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        self.slots=[[] for _ in range(16)]
        self.slot_length=16
        self.count=0

    def __rehash(self):
        if self.count*2<=self.slot_length:
            return
        self.count=0
        self.slot_length*=2
        old_slots=self.slots
        self.slots=[[] for _ in range(self.slot_length)]
        for slot in old_slots:
            for key in slot:
                self.add(key)

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        hash=key%self.slot_length
        self.slots[hash].append(key)
        self.count+=1
            

    def remove(self, key: int) -> None:
        hash=key%self.slot_length
        slot=self.slots[hash]
        for i in range(len(slot)):
            if slot[i]==key:
                slot[i]=slot[-1]
                slot.pop()
                return True
        return False

    def contains(self, key: int) -> bool:
        hash=key%self.slot_length
        slot=self.slots[hash]

        for n in slot:
            if n==key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

myHashSet =MyHashSet()
myHashSet.add(1)      # set = [1]
myHashSet.add(2)      # set = [1, 2]
myHashSet.contains(1) # 返回 True
myHashSet.contains(3) # 返回 False ，（未找到）
myHashSet.add(2)      # set = [1, 2]
myHashSet.contains(2) # 返回 True
myHashSet.remove(2)   # set = [1]
myHashSet.contains(2) # 返回 False ，（已移除）