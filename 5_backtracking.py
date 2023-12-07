def knapSack(W, wt, val, n, memo={}):
    if n == 0 or W == 0:
        return 0

    # Check if the result is already memoized
    if (n, W) in memo:
        return memo[(n, W)]

    if wt[n - 1] > W:
        result = knapSack(W, wt, val, n - 1, memo)
    else:
        result = max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1, memo),
            knapSack(W, wt, val, n - 1, memo)
        )

    # Memoize the result before returning
    memo[(n, W)] = result
    return result

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

result = knapSack(W, wt, val, n)
print("Maximum value that can be obtained:", result)
