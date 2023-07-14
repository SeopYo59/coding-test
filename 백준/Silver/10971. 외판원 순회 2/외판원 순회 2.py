def simul_route(i_to_j_costs, pos, route, sum_cost ):
    if len(route) == len(i_to_j_costs[0]):
        if i_to_j_costs[pos][route[0]] == 0:
            return
        else:
            results.append(sum_cost + i_to_j_costs[pos][route[0]])

    for j in range( len(i_to_j_costs[pos]) ):
         if (j not in route) and (i_to_j_costs[pos][j] != 0):
            temp_route = route.copy()
            temp_route.append(j)
            simul_route(i_to_j_costs, j, temp_route, sum_cost + i_to_j_costs[pos][j])

N = int(input())

i_to_j_costs = []
for i in range(N):
    cost = list(map(int, input().split(" ")))
    i_to_j_costs.append(cost)

results =[]
for i in range(N):
    pos = i
    route = []
    route.append(i)
    sum_cost = 0
    simul_route(i_to_j_costs, i, route.copy(), sum_cost)

print(min(results))

