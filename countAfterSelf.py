def countAfterSelf(nums):
    res = []
    for i in range(len(nums)):
        count = 0
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                count+=1

        res.append(count)
    return res

nums = list(map(int,input().strip().split()))
print(countAfterSelf(nums))
