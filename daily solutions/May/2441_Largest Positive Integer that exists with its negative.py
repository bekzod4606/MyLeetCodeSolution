def findMaxK(nums):
    setnum = set(nums)
    ready = []
    for x in setnum:
        if -x in setnum:
            ready.append(x)
    return max(ready, default=-1)