def tsp(graph, v, n, current_pos, cost, count, ans):
    if count == n and graph[current_pos][0] > 0:
        ans = min(ans, cost + graph[current_pos][0])
        return ans
    
    for i in range(n):
        if not v[i] and graph[current_pos][i] > 0:
            v[i] = True

            ans = tsp(graph, v, n, i, cost + graph[current_pos][i], count + 1, ans)

            v[i] = False
    
    return ans

def main():
    n = 4

    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    v = [False] * n
    ans = float('inf')

    v[0] = True

    ans = tsp(graph, v, n, 0, 0, 1, ans)

    print(ans)

if __name__ == "__main__":
    main()
