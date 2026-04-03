class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        least = 1
        most = max(piles)

        eating_speed = least

        while least <= most:

            mid_speed = (least + most) // 2
            curr_time = 0

            for b in piles:
                
                curr_time += math.ceil(b/mid_speed)
            
            if curr_time <= h:
                eating_speed = mid_speed
                most = mid_speed - 1
            else:
                least = mid_speed + 1
        
        return eating_speed
