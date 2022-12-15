def difference(nums):

    if len(nums) > 0:
        res = max(nums) - min(nums)
    else:
        res = 0
    return res


print(round(difference((10.2, -2.2, 0, 1.1, 0.5)), 2))
