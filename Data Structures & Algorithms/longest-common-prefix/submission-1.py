class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        target = len(min(strs, key=len))
        for i in range(target):
            char = strs[0][i]
            if not all(s[i]==char for s in strs): return strs[0][:i]
        return strs[0][:target]
