"""
Experiment 04 - Longest Common Subsequence (LCS) using Dynamic Programming (CO-2)
"""


def lcs(x, y):
    m, n = len(x), len(y)
    # dp[i][j] = length of LCS of x[:i] and y[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to build the LCS string
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            result.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], "".join(reversed(result))


if __name__ == "__main__":
    seq1 = "ABCBDAB"
    seq2 = "BDCABA"
    length, subsequence = lcs(seq1, seq2)
    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)
    print("Length of LCS:", length)
    print("LCS:", subsequence)
