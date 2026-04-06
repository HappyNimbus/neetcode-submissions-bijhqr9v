class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        least = 1
        most = max(piles)

        eat_time = least

        while least <= most:
            
            mid = (least + most)//2
            
            total_hours = 0
            #check eating speed
            for pile in piles:
                total_hours += (pile + mid - 1)//mid
            
            if total_hours <= h:
                eat_time = mid
                most = mid - 1
            else:
                least = mid + 1

        return eat_time