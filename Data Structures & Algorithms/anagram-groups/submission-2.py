class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {tuple(sorted(s)): [] for s in strs}
        for s in strs:
            ht[tuple(sorted(s))].append(s)
        
        return list(ht.values())

