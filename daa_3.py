
def knapsack(weights, values, capacity, n):

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    # Find selected items
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i)
            w -= weights[i-1]

    selected.reverse()

    print("Maximum Profit:", dp[n][capacity])
    print("Selected Items:", selected)


# Main Program
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i+1}: "))
    value = int(input(f"Enter profit of item {i+1}: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter knapsack capacity: "))

knapsack(weights, values, capacity, n)
