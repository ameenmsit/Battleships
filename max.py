def getMax(li):
    max=None
    for i in li:
        if(max == None or max <i):
            max=i
    return max

print(getMax([1,23,54,21,78,10,29]))