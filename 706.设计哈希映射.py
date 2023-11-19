#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        self.base=7
        self.slots=[[] for _ in range(self.base)]
        self.count=0

    def put(self, key: int, value: int) -> None:
        hash=key%self.base
        for entry in self.slots[hash]:
            if entry[0]==key:
                entry[1]=value
                return
        self.slots[hash].append([key,value])
        self.count+=1

        if self.count*2<self.base:
            return
        
        self.base=self.base*2-1
        self.count=0
        old_slots=self.slots
        self.slots=[[] for _ in range(self.base)]
        for slot in old_slots:
            for key,val in slot:
                self.put(key,val)

    def get(self, key: int) -> int:
        hash=key%self.base
        for entry in self.slots[hash]:
            if entry[0]==key:
                return entry[1]
        return -1

    def remove(self, key: int) -> None:
        hash=key%self.base
        slot=self.slots[hash]
        for i,entry in enumerate(slot):
            if entry[0]==key:
                slot[i]=slot[-1]
                slot.pop()
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

