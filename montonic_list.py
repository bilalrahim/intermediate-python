
nums=[1,2,3,4,5,6]
monotone_increasing, monotone_decreasing=False, False
index=0

while index < len(nums) - 1:
    if nums[index] == nums[index+1]:
        index+=1
        continue
    elif nums[index] < nums[index+1]:
        monotone_increasing=True
        break
    else:
        monotone_decreasing=True
        break

index=0
if monotone_increasing:
    while index < len(nums) - 1:
        if nums[index] <= nums[index+1]:
            index+=1
            continue
        else:
            print("not monotone")
else:
    while index < len(nums) - 1: 
        if nums[index] >= nums [index+1]:
            index+=1
            continue
        else:
            print("not monotone")
            