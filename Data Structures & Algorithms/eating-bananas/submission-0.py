class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        min_speed = r
        #1,2,3,4 - 9
        #4,10,23,25 - 4
        while l <= r:

            speed = (l+r)//2
    
            if self.canFinish(speed, piles, h):
                min_speed = min(min_speed, speed)
                r = speed - 1
            else:
                l = speed + 1

        return min_speed


    def canFinish(self, speed, piles: List[int], h: int) -> bool:

        time_to_finish = 0

        for n in piles:
            time_to_finish += math.ceil(n / speed)
            if time_to_finish > h:
                return False
            
        if time_to_finish <= h:
            return True
        else:
            return False

