#
# @lc app=leetcode.cn id=1865 lang=python3
#
# [1865] 找出和为指定值的下标对
#
from sbw import *
# @lc code=start
from sortedcontainers import SortedDict
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2=nums2
        self.counter1=Counter(nums1)
        self.counter2=Counter(nums2)

    def add(self, index: int, val: int) -> None:
        
        old=self.nums2[index]
        if self.counter2[old]==1:
            self.counter2.pop(old)
        else:
            self.counter2[old]-=1
        self.counter2[old+val]=self.counter2.get(old+val,0)+1
        self.nums2[index]+=val


    def count(self, tot: int) -> int:
        ret=0
        for x,v in self.counter1.items():
            ret+=v*self.counter2[tot-x]
        return ret


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end

findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])#
assert findSumPairs.count(7)==8#  # 返回 8 # 下标对 (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) 满足 2 + 5 = 7 ，下标对 (5,1), (5,5) 满足 3 + 4 = 7
findSumPairs.add(3, 2)# # 此时 nums2 = [1,4,5,4,5,4]
assert findSumPairs.count(8)==2#  # 返回 2 ；下标对 (5,2), (5,4) 满足 3 + 5 = 8
assert findSumPairs.count(4)==1#  # 返回 1 ；下标对 (5,0) 满足 3 + 1 = 4
findSumPairs.add(0, 1)# # 此时 nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1)# # 此时 nums2 = [2,5,5,4,5,4]
assert findSumPairs.count(7)==11#  # 返回 11 ；下标对 (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) 满足 2 + 5 = 7 ，下标对 (5,3), (5,5) 满足 3 + 4 = 7