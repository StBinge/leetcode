#
# @lc app=leetcode.cn id=2353 lang=python3
# @lcpr version=30204
#
# [2353] 设计食物评分系统
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map={food:[cu,rat] for cu,food,rat in zip(cuisines,foods,ratings)}
        groups=defaultdict(list)
        for cu,rat,food in zip(cuisines,ratings,foods):
            heapq.heappush(groups[cu],[-rat,food])
        self.groups=groups

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_map[food][1]=newRating
        heapq.heappush(self.groups[self.food_map[food][0]],[-newRating,food])

    def highestRated(self, cuisine: str) -> str:
        while True:
            rat,food=self.groups[cuisine][0]
            if self.food_map[food][1]==-rat:
                return food
            heapq.heappop(self.groups[cuisine])


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end
test_obj(FoodRatings,["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"],[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]],'[null, "kimchi", "ramen", null, "sushi", null, "ramen"]')


