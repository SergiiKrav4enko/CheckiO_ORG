def check(data=[]):
    data.sort()
    a=len(data)
    print(data)
    if a%2 == 0:
        median_1=a//2
        median=(data[median_1]+data[median_1-1])/2
    else:
        median_1=a//2
        median=data[median_1]
    return median
print(check([1,2,3,4,5]))