def find_duplicate(nums):
    if not verify_list(nums):
        return False

    nums.sort()

    for i in range(len(nums)):
        for aux in nums[i + 1:]:
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
    if len(nums) <= 1:
        return False
    if not isinstance(nums, list):
        return False
    return verify_string_and_not_negative_in_list(nums)


def verify_string_and_not_negative_in_list(nums):
    for number in nums:
        if not isinstance(number, int):
            return False
        elif number < 0:
            return False
    return True


if __name__ == "__main__":
    list_nums = [52, 99, 58, 20, 6, 999, 5, 41, 38, 9]
    print(find_duplicate(list_nums))
