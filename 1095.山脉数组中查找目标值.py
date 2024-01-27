#
# @lc app=leetcode.cn id=1095 lang=python3
#
# [1095] 山脉数组中查找目标值
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def __init__(self,arr) -> None:
       self.arr=arr
       self.cnt=0
   def get(self, index: int) -> int:
       self.cnt+=1
       if self.cnt>=100:
           raise "Call too many times!"
       return self.arr[index]
   def length(self) -> int:
       return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        Max=100000
        def find(left,right):
            if left==right and mountain_arr.get(left)==target:
                return left
            if left>=right:
                return Max
            mid=(left+right)>>1
            mid_v=mountain_arr.get(mid)
            if mid_v==target:
                if mid_v<mountain_arr.get(mid+1):
                    return mid
                return min(mid,find(left,mid-1))
            if mid_v>target:
                idx=find(left,mid-1)
                if idx!=Max:
                    return idx
                return find(mid+1,right)
            if mid_v<target:
                if mid_v>mountain_arr.get(mid+1):
                    return find(left,mid-1)
                return find(mid+1,right)
        ret=find(0,mountain_arr.length()-1)
        return ret if ret!=Max else -1
# @lc code=end
arr=MountainArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82])
assert Solution().findInMountainArray(1,arr)==0
arr=MountainArray([3,5,3,2,0])
assert Solution().findInMountainArray(3,arr)==0
arr=MountainArray([0,1,2,4,2,1])
assert Solution().findInMountainArray(3,arr)==-1
arr=MountainArray([1,2,3,4,5,3,1])
assert Solution().findInMountainArray(3,arr)==2
