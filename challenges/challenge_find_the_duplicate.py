def find_duplicate(nums):
    result = verify_list(nums)
    if not result:
        return False

    merge_sort(nums, 0, len(nums))
    result = find_duplicate_aux(nums, 0, 1)
    return result


def find_duplicate_aux(nums, number, next):
    size = len(nums)
    if nums[number] == nums[next]:
        return nums[number]
    elif number + 1 == size - 1:
        return False
    elif next + 1 == size:
        return find_duplicate_aux(nums, number + 1, number + 2)
    else:
        return find_duplicate_aux(nums, number, next + 1)


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


def merge_sort(list_strings, start=0, end=None):
    if end is None:
        end = len(list_strings)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(list_strings, start, mid)
        merge_sort(list_strings, mid, end)
        merge(list_strings, start, mid, end)


def merge(list_strings, start, mid, end):
    left = list_strings[start:mid]
    right = list_strings[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            list_strings[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            list_strings[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            list_strings[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            list_strings[general_index] = right[right_index]
            right_index = right_index + 1


if __name__ == "__main__":
    list_nums = [5, 8, 3, 20, 20, 6, 9, 41]
    print(find_duplicate(list_nums))
