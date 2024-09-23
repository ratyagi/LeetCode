def maxProfit(prices) -> int:
    profit =0 

    for i in range (1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += (prices[i] - prices[i-1])
    return profit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = maxProfit(prices)
    print("Maximum profit:", max_profit)

if __name__ == "__main__":
    main()