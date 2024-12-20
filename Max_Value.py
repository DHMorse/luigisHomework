# Max_Value.py


def max_value(nums):
    max = nums[0]
    for x in nums:
        if x > max:
            max = x
    return max


numbers = [45, 4, 78, 95, 419, -40, 12]

print(max_value(numbers))
