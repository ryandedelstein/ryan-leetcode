def twoSum(nums, target):
    storage = {}
    curr = 0
    for i in nums:
        need = target - i
        if storage.get(need) != None:
            return [storage.get(need), curr]
        else:
            storage[i] = curr
            curr = curr + 1
