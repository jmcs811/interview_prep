def coinChange(coins, amount):
    dp = [0]+ (float('inf') * amount) 

    for i, val in enumerate(dp):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    min_coins = dp[-1]
    if min_coins == float('inf'):
        return -1

    return min_coins