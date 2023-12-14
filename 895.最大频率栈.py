#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
import heapq
# class LinkNode:
#     def __init__(self,val) -> None:
#         self.val=val
#         self.prev=None
#         self.next=None
class FreqStack:

    def __init__(self):
        self.max_freq=0
        self.freq_bucks={}
        self.freq={}

    def push(self, val: int) -> None:
        f=self.freq.get(val,0)+1
        self.freq[val]=f
        self.freq_bucks.setdefault(f,[]).append(val)
        if f>self.max_freq:
            self.max_freq=f

    def pop(self) -> int:
        val=self.freq_bucks[self.max_freq].pop()
        self.freq[val]-=1
        if len(self.freq_bucks[self.max_freq])==0:
            self.max_freq-=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end
freqStack =FreqStack()
freqStack.push (5)#堆栈为 [5]
freqStack.push (7)#堆栈是 [5,7]
freqStack.push (5)#堆栈是 [5,7,5]
freqStack.push (7)#堆栈是 [5,7,5,7]
freqStack.push (4)#堆栈是 [5,7,5,7,4]
freqStack.push (5)#堆栈是 [5,7,5,7,4,5]
assert freqStack.pop ()==5#返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
assert freqStack.pop ()==7#返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
assert freqStack.pop ()==5#返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
assert freqStack.pop ()==4#返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
