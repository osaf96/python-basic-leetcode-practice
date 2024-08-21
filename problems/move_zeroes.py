def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeroIndex = -1
    
    for i in range(len(nums)):
        if nums[i] != 0 and zeroIndex > -1: 
            nums[zeroIndex] = nums[i]
            nums[i] = 0
            if nums[zeroIndex + 1] == 0:
                zeroIndex = zeroIndex + 1
            else:
                zeroIndex = -1 
        else:
            if nums[i] == 0 and zeroIndex == -1:
                zeroIndex = i 
    print(nums)
    
    
moveZeroes([0,0,1,3,7,9])