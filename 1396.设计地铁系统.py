#
# @lc app=leetcode.cn id=1396 lang=python3
#
# [1396] 设计地铁系统
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.time_memo={}
        self.passengers={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station,start_time=self.passengers[id]
        spend=t-start_time
        counter=self.time_memo.setdefault((start_station,stationName),[0,0])
        counter[0]+=spend
        counter[1]+=1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tot,cnt=self.time_memo.get((startStation,endStation))
        return tot/cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

