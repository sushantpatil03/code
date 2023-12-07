def knapSack(W, wt, val, n):
    # Base case: If either the number of items or the knapsack capacity is zero
    if n == 0 or W == 0:
        return 0

    # If the weight of the nth item is more than the knapsack capacity,
    # then this item cannot be included in the optimal solution
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)

    # Return the maximum of two cases:
    # 1. nth item included
    # 2. nth item not included
    return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
               knapSack(W, wt, val, n - 1))


# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

result = knapSack(W, wt, val, n)
print("Maximum value that can be obtained:", result)
