class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        mp={}
        for i in arr:
            if i not in mp:
                mp[i]=0
            mp[i]+=1

        final = []
        for i in range(k):
            maxfreq =-1
            for i in list(mp.keys()):
                if maxfreq < mp[i]:
                    maxfreq = mp[i]
                    temp = i

            mp[temp] = 0
            final.append(temp)

        return final