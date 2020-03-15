def sum_of_multiples(limit, multiples):
    return sum(set([y for x in multiples for y in range(1, limit) if x != 0 and y % x == 0]))
