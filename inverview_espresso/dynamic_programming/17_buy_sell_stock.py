class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        TIME: O(n)
        SPACE: O(1)
        '''
        lowest = float('inf')
        best = 0
        
        for i in prices:
            if i < lowest:
                lowest = i
            
            profit = i - lowest
            if profit > best:
                best = profit
                
        return max(best, 0)