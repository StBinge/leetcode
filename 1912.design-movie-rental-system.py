#
# @lc app=leetcode.cn id=1912 lang=python3
# @lcpr version=30204
#
# [1912] 设计电影租借系统
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        ordered_movie=defaultdict(SortedList)
        self.ordered_rent=SortedList()
        price_dict={}

        for shop,mov,p in entries:
            ordered_movie[mov].add([p,shop])
            price_dict[shop,mov]=p
        self.ordered_movies=ordered_movie
        self.price_dict=price_dict

    def search(self, movie: int) -> List[int]:
        return [m[1] for m in self.ordered_movies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        self.ordered_rent.add([self.price_dict[shop,movie],shop,movie])
        self.ordered_movies[movie].remove([self.price_dict[shop,movie],shop])

    def drop(self, shop: int, movie: int) -> None:
        p=self.price_dict[shop,movie]
        self.ordered_rent.remove([p,shop,movie])
        self.ordered_movies[movie].add([p,shop])

    def report(self) -> List[List[int]]:
        return [[rent[1],rent[2]] for rent in self.ordered_rent[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
# @lc code=end


movieRentingSystem = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
assert movieRentingSystem.search(1)==[1,0,2];  # 返回 [1, 0, 2] ，商店 1，0 和 2 有未借出的 ID 为 1 的电影。商店 1 最便宜，商店 0 和 2 价格相同，所以按商店编号排序。
movieRentingSystem.rent(0, 1); # 从商店 0 借出电影 1 。现在商店 0 未借出电影编号为 [2,3] 。
movieRentingSystem.rent(1, 2); # 从商店 1 借出电影 2 。现在商店 1 未借出的电影编号为 [1] 。
assert movieRentingSystem.report()==[[0, 1], [1, 2]] 
movieRentingSystem.drop(1, 2); # 在商店 1 返还电影 2 。现在商店 1 未借出的电影编号为 [1,2] 。
assert movieRentingSystem.search(2)==[0, 1]
#
# @lcpr case=start
# ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"][[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]\n
# @lcpr case=end

#

