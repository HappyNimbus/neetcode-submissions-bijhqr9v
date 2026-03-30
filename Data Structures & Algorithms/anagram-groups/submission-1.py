class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hMap= defaultdict(list)
        #key = secret ord number, value = word

        for s in strs:

            arr = [0]*26

            for c in s:

                pst = ord(c) - ord('a')
                arr[pst] += 1
            
            tArr = tuple(arr)
            hMap[tArr].append(s)
        
        return (list(hMap.values()))