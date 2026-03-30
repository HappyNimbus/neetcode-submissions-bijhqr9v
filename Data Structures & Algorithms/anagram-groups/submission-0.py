class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hMap = {}

        for s in strs:

            count = [0] * 26

            for c in s:
                letter = (ord(c) - ord('a'))
                count[letter] += 1
            
            tupleCount = tuple(count)
            
            if tupleCount not in hMap:
                hMap[tupleCount] = []
            hMap[tupleCount].append(s)

        return list(hMap.values())
        

        