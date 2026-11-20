"""
Experiment 06 - Calculate the nth Fibonacci number efficiently (CO-2)
Compares Memoization (top-down), Tabulation (bottom-up) and space-optimized DP.
"""
import time


# ---------- Top-down (Memoization) ----------
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ---------- Bottom-up (Tabulation) ----------
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# ---------- Space optimized: O(n) time, O(1) space ----------
def fib_optimized(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    n = int(input("Enter n: ") or 10)

    for name, func in [("Memoization", fib_memo),
                       ("Tabulation", fib_tab),
                       ("Space optimized", fib_optimized)]:
        start = time.perf_counter()
        result = func(n)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"{name:<16}: F({n}) = {result}  ({elapsed:.4f} ms)")
