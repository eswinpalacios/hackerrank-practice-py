def crush(n=0, m=[]):
    result = []

    for i in range(n):
        result.append(0)

    for e in m:
        operation(e[0], e[1], e[2], result)

    return max(result)


def operation(index_from, index_end, number, table):
    for i in range(index_from - 1, index_end):
        table[i] = table[i] + number


queries = [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1]
]
print(crush(10, queries))
