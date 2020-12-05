def grid_traveler(m, n, cache = {}):
    if (m, n) in cache:
        return cache[(m, n)]
    if 0 in [m, n]:
        return 0
    if 1 in [m, n]:
        return 1

    cache[(m, n)] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1)
    return cache[(m, n)]