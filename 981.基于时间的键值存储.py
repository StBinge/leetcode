#
# @lc app=leetcode.cn id=981 lang=python3
#
# [981] 基于时间的键值存储
#
from sbw import *
# @lc code=start
import bisect
class TimeMap:

    def __init__(self):
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict.setdefault(key,[]).append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        values=self.dict.get(key,None)
        if not values:
            return ''
        idx=bisect.bisect_right(values,timestamp,key=lambda x:x[0])
        idx-=1
        if idx<0:
            return ''
        return values[idx][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
methods=["TimeMap", "set", "get", "get", "set", "get", "get"]
args=[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
ret='[null, null, "bar", "bar", null, "bar2", "bar2"]'
ret=format_array(ret)
obj = TimeMap()
for i in range(1,len(methods)):
    func=getattr(obj,methods[i])
    r=func(*args[i])
    assert r==ret[i]
