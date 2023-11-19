#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
import random
class RandomizedCollection:

    def __init__(self):
        self.nums=[]
        self.indices:dict[int,set]={}

    def insert(self, val: int) -> bool:
        flag=False
        ids=self.indices.setdefault(val,set())
        if not ids:
            flag=True
        self.nums.append(val)
        ids.add(len(self.nums)-1)
        return flag


    def remove(self, val: int) -> bool:
        ids=self.indices.get(val,None)
        if not ids:
            return False
        id=ids.pop()
        if id!=len(self.nums)-1:
            swapped_val=self.nums[-1]
            self.nums[id]=swapped_val
            swapped_ids=self.indices[swapped_val]
            swapped_ids.remove(len(self.nums)-1)
            swapped_ids.add(id)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

obj = RandomizedCollection()
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_1 = obj.insert(1)
