#
# @lc app=leetcode.cn id=900 lang=python3
#
# [900] RLE 迭代器
#
from typing import List
# @lc code=start
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding=encoding
        self.cur_idx=0
        self.deleted=0

    def next(self, n: int) -> int:
        while self.cur_idx<len(self.encoding):
       
            if self.deleted+n>self.encoding[self.cur_idx]:
                n-=self.encoding[self.cur_idx]-self.deleted

                self.deleted=0
                self.cur_idx+=2
            else:
                self.deleted+=n
                return self.encoding[self.cur_idx+1]
        return -1




# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
# @lc code=end
rLEIterator = RLEIterator([3, 8, 0, 9, 2, 5]) # 这映射到序列 [8,8,8,5,5]。
assert rLEIterator.next(2)==8 # 耗去序列的 2 个项，返回 8。现在剩下的序列是 [8, 5, 5]。
assert rLEIterator.next(1)==8 # 耗去序列的 1 个项，返回 8。现在剩下的序列是 [5, 5]。
assert rLEIterator.next(1)==5 # 耗去序列的 1 个项，返回 5。现在剩下的序列是 [5]。
assert rLEIterator.next(2)==-1 # 耗去序列的 2 个项，返回 -1。 这是由于第一个被耗去的项是 5，
