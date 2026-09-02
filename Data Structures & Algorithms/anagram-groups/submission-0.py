class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        # for i in range(len(arr)):
        #     print(arr[i],end=" ")

        mp = {}

        for word in arr:
            freq = [0]*26

            for c in word:
                freq[ord(c)-ord('a')]+=1

            key = tuple(freq)
            if key not in mp:
                mp[key] = []
            mp[key].append(word)

        return list(mp.values())