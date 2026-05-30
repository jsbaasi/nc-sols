class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        3,1,2,4
        '''
        count = Counter(hand)
        hand.sort()
        if len(hand)%groupSize: return False
        for h in hand:
            if not count[h]: continue
            for _ in range(groupSize):
                count[h]-=1
                if count[h]<0: return False
                h+=1
        return True