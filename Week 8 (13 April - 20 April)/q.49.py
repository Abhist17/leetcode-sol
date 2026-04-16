from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            mp[key].append(word)
        return list(mp.values())