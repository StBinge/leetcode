#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#
# class DictTree:
#     def __init__(self) -> None:
#         self.slots=[None]*26
#         self.value=0
# @lc code=start
class MapSum:

    def __init__(self):
        self.slots=[None]*26
        self.value=0
        self.memo={}

    def insert(self, key: str, val: int) -> None:
        v=val-self.memo.get(key,0)
        cur=self
        for ch in key:
            idx=ord(ch)-ord('a')
            if not cur.slots[idx]:
                cur.slots[idx]=MapSum()
            cur=cur.slots[idx]
            cur.value+=v
        self.memo[key]=val

    def sum(self, prefix: str) -> int:
        cur=self

        for ch in prefix:
            idx=ord(ch)-ord('a')
            cur=cur.slots[idx]
            if not cur:
                return 0

        return cur.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

mapSum=MapSum()
mapSum.insert("apple", 3) 
assert mapSum.sum("ap")==3
mapSum.insert("app", 2)
assert mapSum.sum("ap")==5
assert mapSum.sum("appp")==0
mapSum.insert('apple',5)
assert mapSum.sum('apple')==5

mapSum.insert('apple',1)
assert mapSum.sum('apple')==1