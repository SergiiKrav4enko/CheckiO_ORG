def check(data=[]):
    result = []
    a=(len(data))
    for el in range(a):
        if data.count(data[el]) > 1:
            result.append(data[el])
    return result
print(check([1,2,3,1,3]))