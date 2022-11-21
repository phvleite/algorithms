def find_duplicate(nums):
    result = verify_list(nums)
    if not result:
        return False

    nums.sort()

    for i in range(len(nums)):
        nums_aux = nums[i + 1:]
        for aux in nums_aux:
            if nums[i] == aux:
                return aux

    return False


# def find_duplicate_aux(nums, number, next, size):
#     if nums[number] == nums[next]:
#         return nums[number]
#     elif number + 1 == size - 1:
#         return False
#     elif next + 1 == size:
#         return find_duplicate_aux(nums, number + 1, number + 2, size)
#     else:
#         return find_duplicate_aux(nums, number, next + 1, size)


def verify_list(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False
    if not isinstance(nums, list):
        return False
    if not verify_string_in_list(nums):
        return False
    if not verify_not_negative_in_list(nums):
        return False

    return True


def verify_string_in_list(nums):
    for number in nums:
        result = isinstance(number, int)
        if not result:
            return result
    return True


def verify_not_negative_in_list(nums):
    for number in nums:
        if number < 0:
            return False
    return True


if __name__ == "__main__":
    list_nums = [5, 99, 58, 20, 6, 9, 5, 41]
    print(find_duplicate(list_nums))
