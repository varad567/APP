"""
Experiment 05 - 0/1 Knapsack Problem (CO-2)
Optimal selection of items to maximize value within a weight constraint
using Bottom-up (Tabulation) and Top-down (Memoization) approaches.
"""


# ---------- Bottom-up approach (Tabulation) ----------
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    # Find which items were selected
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1]


# ---------- Top-down approach (Memoization) ----------
def knapsack_top_down(weights, values, capacity):
    memo = {}

    def solve(i, w):
        if i == 0 or w == 0:
            return 0
        if (i, w) in memo:
            return memo[(i, w)]
        if weights[i - 1] > w:
            memo[(i, w)] = solve(i - 1, w)
        else:
            memo[(i, w)] = max(values[i - 1] + solve(i - 1, w - weights[i - 1]),
                               solve(i - 1, w))
        return memo[(i, w)]

    return solve(len(weights), capacity)


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7

    print("Weights :", weights)
    print("Values  :", values)
    print("Capacity:", capacity)

    best, items = knapsack_bottom_up(weights, values, capacity)
    print("\nBottom-up maximum value:", best)
    print("Selected item indices  :", items)

    print("\nTop-down maximum value :", knapsack_top_down(weights, values, capacity))
