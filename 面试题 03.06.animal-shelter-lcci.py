#
# @lc app=leetcode.cn id=面试题 03.06 lang=python3
# @lcpr version=30204
#
# [面试题 03.06] 动物收容所
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class AnimalShelf:

    def __init__(self):
        self.slots=[deque(maxlen=20000),deque(maxlen=20000)]

    def enqueue(self, animal: List[int]) -> None:
        self.slots[animal[1]].append(animal[0])

    def dequeueAny(self) -> List[int]:
        if not self.slots[0] and not self.slots[1]:
            return [-1,-1]
        if not self.slots[0]:
            return [self.slots[1].popleft(),1]
        if not self.slots[1]:
            return [self.slots[0].popleft(),0]
        if self.slots[0][0]>self.slots[1][0]:
            return [self.slots[1].popleft(),1]
        return [self.slots[0].popleft(),0]

    def dequeueDog(self) -> List[int]:
        if not self.slots[1]:
            return [-1,-1]
        return [self.slots[1].popleft(),1]
    
    def dequeueCat(self) -> List[int]:
        if not self.slots[0]:
            return [-1,-1]
        return [self.slots[0].popleft(),0]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
# @lc code=end
obj=AnimalShelf()
ops=["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
args=[[], [[0, 0]], [[1, 0]], [], [], []]
ret='[null,null,null,[0,0],[-1,-1],[1,0]]'
test_obj(obj,ops,args,ret)

#
# @lcpr case=start
# ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"][[], [[0, 0]], [[1, 0]], [], [], []]\n
# @lcpr case=end

# @lcpr case=start
# ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"][[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]\n
# @lcpr case=end

#

