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

    def add(self, number: int,delta=1) -> None:
        freq=self.val_freq[number]
        self.freq_freq[freq]-=1
        freq+=delta
        self.val_freq[number]=freq
        self.freq_freq[freq]+=1

    def deleteOne(self, number: int) -> None:
        if self.val_freq[number]>0:
            self.add(number,-1)


    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_freq[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
# @lc code=end
test_obj(FrequencyTracker,["FrequencyTracker","hasFrequency","add","add","deleteOne","deleteOne","add","deleteOne","add","add","hasFrequency","hasFrequency","deleteOne","add","add","add","deleteOne","hasFrequency","deleteOne","add","deleteOne","add","deleteOne","deleteOne","hasFrequency","deleteOne","deleteOne","deleteOne","hasFrequency","deleteOne","hasFrequency","deleteOne","hasFrequency","add"],[[],[1],[9],[7],[5],[9],[10],[3],[2],[5],[1],[1],[7],[9],[7],[7],[3],[1],[9],[8],[10],[7],[6],[10],[2],[5],[7],[2],[1],[5],[1],[6],[2],[3]],'[null,false,null,null,null,null,null,null,null,null,true,true,null,null,null,null,null,true,null,null,null,null,null,null,false,null,null,null,true,null,true,null,true,null]')
test_obj(FrequencyTracker,["FrequencyTracker", "add", "add", "hasFrequency"],[[], [3], [3], [2]],'[null, null, null, true]')


