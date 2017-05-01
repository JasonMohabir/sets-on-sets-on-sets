def union(x, y):
    return [i for i in x if i not in y] + y

def intersection(x, y):
    return [i for i in x if i in y]

def setdiff(x, y):
    return [i for i in x if i not in y]

def symdiff(x, y):
    return setdiff(union(x, y), intersection(x, y))

def cartprod(x, y):
    return [(i, j) for i in x for j in y]

# Testing
a = [1, 2]
b = [2, 3, 4]
print union(a, b)
print intersection(a, b)
print setdiff(a, b)
print symdiff(a, b)
print cartprod(a, b)
