class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        profit = 0
        while right < len(prices):
            if prices[right]-prices[left] > profit:
                profit = prices[right]-prices[left]
            elif prices[right] < prices[left]:
                left=right
            right+=1
        return profit
        

def main():
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    max_profit = solution.maxProfit(prices)
    print("Maximum profit:", max_profit)

if __name__ == "__main__":
    main()
