def is_anagram(first_string, second_string):

    if len(first_string) != 0:
        first_string = check_if_is_anagram(first_string)

    if len(second_string) != 0:
        second_string = check_if_is_anagram(second_string)

    if first_string == second_string and (
        len(first_string) > 0 and len(second_string) > 0
    ):
        return (first_string, second_string, True)
    elif len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)
    else:
        return (first_string, second_string, False)


def check_if_is_anagram(string):
    string = string.lower()
    list_string = convert_strings_to_list(string)
    merge_sort(list_string, 0, len(list_string))
    string = convert_list_to_strings(list_string)
    return string


def convert_strings_to_list(string):
    list_string = []
    for w in string:
        list_string.append(w)

    return list_string


def convert_list_to_strings(list):
    return "".join(list)


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


if __name__ == "__main__":
    result = is_anagram("opta", "pato")
    print(result)
