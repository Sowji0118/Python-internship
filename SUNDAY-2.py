def ans(nums):
    n=len(nums)
    result=[-1]*n
    for i in range(n):
        for j in range(1,n):
            if(nums[(i+j)%n]>nums[i]):
                result[i]=nums[(i+j)%n]
        return result
nums=[1,2,1]
print(ans(nums))
