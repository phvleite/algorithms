def find_duplicate(nums):
    if not verify_list(nums):
        return False

    nums.sort()

    for ind, num in enumerate(nums):
        if ind <= len(nums) - 2 and num == nums[ind + 1]:
            return num
    return False


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
    # list_nums = [52, 99, 53, 20, 6, 999, 5, 41, 38, 9]
    list_nums = [1, 3, 4, 2, 22]
    print(find_duplicate(list_nums))
