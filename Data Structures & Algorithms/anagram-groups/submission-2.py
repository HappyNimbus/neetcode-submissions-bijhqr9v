class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        arr = defaultdict(list)

        for word in strs:

            key = [0]*26

            for c in word:

                number = ord(c) - ord('a')
                key[number] += 1
            
            newKey = tuple(key)
            arr[newKey].append(word)
        
        return list(arr.values())
