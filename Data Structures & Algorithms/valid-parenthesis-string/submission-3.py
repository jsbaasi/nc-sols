class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = len([c for c in s if c=="*"])
        n = len(s)
        curr = 0
        right_stars = left_stars = 0
        for i in range(n):
            c = s[i]
            match c:
                case "(": curr+=1
                case ")": curr-=1
                case "*": right_stars+=1
            if curr<0:
                if not right_stars: return False
                else: right_stars-=1; curr = 0
        curr = 0
        for i in range(n-1, -1, -1):
            c = s[i]
            match c:
                case "(": curr-=1
                case ")": curr+=1
                case "*": left_stars+=1
            if curr<0:
                if not left_stars: return False
                else: left_stars-=1; curr = 0
        return True if left_stars+right_stars>=stars else False