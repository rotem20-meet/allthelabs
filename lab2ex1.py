def make(nums):
    i=0
    r=len(nums)
    nums=[nums[i],nums[r-1]]
    return nums
nums=[42,344]
x= make(nums)
print(x)
