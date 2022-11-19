def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    elif len(word) == 1:
        return True
    elif len(word) == 2 and (word[low_index] == word[high_index]):
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(
            word[1: high_index], 0, len(word[1: high_index]) - 1
        )
