"""
You are given an integer array (denoms) representing coins of different denominations and an integer amount (amt) representing a total amount of money.
Find the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1;
"""

# Time Complexity = O(len(coins) * amount)
# Space Complexity = O(amount)
def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    memo = [float('inf')] * (amount + 1)
    # base cases
    for coin in coins:
        if coin < amount + 1:
            memo[coin] = 1
    for i in range(1, amount + 1):
        minCoins = float('inf')
        for coin in coins:
            if i > coin:
                minCoins = min(minCoins, memo[i-coin] + 1)
        memo[i] = min(memo[i], minCoins)
        
        
    return memo[amount] if memo[amount] != float("inf") else -1