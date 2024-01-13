#
# @lc app=leetcode.cn id=1146 lang=python3
#
# [1146] 快照数组
#

# @lc code=start
import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.slots=[[[0,0]] for _ in range(length)]
        self.sid=0

    def set(self, index: int, val: int) -> None:
        slot=self.slots[index]
        while slot and slot[-1][0]==self.sid:
            slot.pop()
        slot.append([self.sid,val])

    def snap(self) -> int:
        self.sid+=1
        return self.sid-1

    def get(self, index: int, snap_id: int) -> int:
        slot=self.slots[index]
        idx=bisect.bisect_right(slot,snap_id,key=lambda x:x[0])
        # if idx<len(slot) and slot[idx][0]<=snap_id:
        #     return slot[idx][1]
        return slot[idx-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end
shot=SnapshotArray(4)
assert shot.snap()==0
assert shot.snap()==1
assert shot.get(3,1)==0
shot.set(2,4)
assert shot.snap()==2
shot.set(1,4)

snapshotArr = SnapshotArray(3)
snapshotArr.set(0,5)
assert snapshotArr.snap()==0
snapshotArr.set(0,6)
assert snapshotArr.get(0,0)==5
snapshotArr.set(0,6)
assert snapshotArr.get(0,1)==6