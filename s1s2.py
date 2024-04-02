def dist(X, x, Y, y):
    if x == 0:
        return y
    if y == 0:
        return x
    c = 0 if (X[x - 1] == Y[y - 1]) else 1
    return min(dist(X, x - 1, Y, y) + 1, dist(X, x, Y, y - 1) + 1, dist(X, x - 1, Y, y - 1) + c)

X = 'rohitkutta'
Y = 'sitting'
print('The Levenshtein distance is', dist(X, len(X), Y, len(Y)))
