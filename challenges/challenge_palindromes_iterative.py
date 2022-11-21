def is_palindrome_iterative(word):
    if len(word) == 0 or (word[0] != word[-1]):
        return False
    elif len(word) == 1:
        return True

    word = word.lower()
    is_palindrome = False
    while len(word) > 0:
        if 3 >= len(word) > 1 and word[0] == word[-1]:
            is_palindrome = True
        word = word[1:-1]

    return is_palindrome


if __name__ == "__main__":
    word = "aniclina"
    print(is_palindrome_iterative(word))
