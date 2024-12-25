#
# @lc app=leetcode.cn id=2671 lang=python3
# @lcpr version=30204
#
# [2671] 频率跟踪器
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class FrequencyTracker:

    def __init__(self):
        self.val_freq=defaultdict(int)
        self.freq_freq=defaultdict(int)

    def add(self, number: int) -> None:
        freq=self.val_freq[number]
        self.freq_freq[freq]-=1
        self.val_freq[number]=freq+1
        self.freq_freq[freq+1]+=1

    def deleteOne(self, number: int) -> None:
        freq=self.val_freq[number]
        if freq==0:
            return
        self.freq_freq[freq]-=1
        self.val_freq[number]=freq-1
        self.freq_freq[freq-1]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_freq[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
# @lc code=end
test_obj(FrequencyTracker,["FrequencyTracker", "add", "add", "hasFrequency"],[[], [3], [3], [2]]
,'[null, null, null, true]')


