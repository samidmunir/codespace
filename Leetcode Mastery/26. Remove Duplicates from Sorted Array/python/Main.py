"""
    26. Remove Duplicates from Sorted Array
    - array (easy)
    
    Giiven an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    
    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
        1. Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
        2. Return k.
    
    Example 1)
        input: nums = [1, 1, 2]
        output: 2, nums = [1, 2, _]
    
    Example 2)
        input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
"""