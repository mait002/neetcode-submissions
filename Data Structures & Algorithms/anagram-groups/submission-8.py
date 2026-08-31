class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = {}
        res = []

        for s in strs:
            freq = [0 for i in range(26)]
            for l in s:
                freq[ord(l.lower()) - ord('a')] += 1
            
            k = str(freq)
            if k in store:
                store[k].append(s)
            else:
                store[k] = [s]
        
        for lst in store:
            res.append(store[lst])

        return res

        


        