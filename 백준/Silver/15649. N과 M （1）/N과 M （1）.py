def permutation(list, list_length, r):
    if r == 1:
        for i in range(list_length):
            list.insert( list_length-1, list.pop(0) )

            results.append(list.copy())
        return

    for i in range(list_length):
        list.insert( list_length-1, list.pop(i) )
        permutation(list, list_length - 1, r - 1)
        list.insert(i, list.pop(list_length-1))

m, n = map(int, input().split())
list = [i+1 for i in range(m)]

results = []
permutation(list, len(list), n)

for result in results:
    for i in range(len(result)-1, (len(result)-1)-n, -1):
        print(result[i], end = " ")

    print("")