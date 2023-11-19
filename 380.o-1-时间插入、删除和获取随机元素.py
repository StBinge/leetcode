#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.nums=[]
        self.indices={}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.nums.append(val)
        self.indices[val]=len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        removed_id=self.indices[val]
        self.nums[removed_id]=self.nums[-1]
        self.indices[self.nums[removed_id]]=removed_id
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

