def knapsack_greedy(items, capacity):
        
    ratios = []
    for i in range(len(items)):
        weight, profit = items[i]
        ratio = profit / weight
        ratios.append((i, ratio))

    
    print("\n Ratios ") 
    print(ratios)
    # Sort items based on the profit-to-weight ratio in descending order
    ratios.sort(key = lambda x:x[1], reverse=True)
    print(ratios)
    
    # Initialize variables
    total_weight = 0
    total_profit = 0
    selected_items = []
    
    # Iterate through the sorted items and add to the knapsack
    for i, _ in ratios:
        if total_weight + items[i][0] <= capacity:
            total_weight += items[i][0]
            total_profit += items[i][1]
            selected_items.append(i)
    
    return {
        "selected_items": selected_items,
        "total_weight": total_weight,
        "total_profit": total_profit
    }

# Test the function with the provided data using lists
items = [
    (3, 10),
    (5, 20),
    (5, 21),
    (8, 30),
    (4, 16)
]

capacity = 20

result = knapsack_greedy(items, capacity)

print("Selected items:", result["selected_items"])
print("Total weight:", result["total_weight"])
print("Total profit:", result["total_profit"])
