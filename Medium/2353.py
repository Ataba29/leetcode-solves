import heapq
from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.heaps = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.heaps:
                self.heaps[c] = []
            heapq.heappush(self.heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.heaps[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
