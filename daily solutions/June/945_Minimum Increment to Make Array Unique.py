def minIncrementForUnique(nums):
        nums.sort()
        count = 0
        length = len(nums)
        for i in range(1, length):
            current, prev = nums[i], nums[i-1]
            if prev>=current:
                dif = prev-current+1
                nums[i]+=dif
                count+=dif
        return count