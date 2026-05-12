class Solution:
    def get_count(self, word:str) -> tuple[int]:
        res = [0]*26
        for c in word:
            res[ord(c)-ord('a')]+=1
        return tuple(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for st in strs:
            groups[self.get_count(st)].append(st)
        return list(groups.values())