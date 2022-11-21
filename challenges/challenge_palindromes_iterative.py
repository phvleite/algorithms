def is_palindrome_iterative(word):
    pass
    # if len(word) == 0 or word[0] != word[-1]:
    #     return False
    # if len(word) == 1:
    #     return True

    # word = word.lower()
    # is_palindrome = False
    # ind = 0
    # ind_max = len(word)
    # for ind in range(len(word)):

    #     if 3 >= len(word) > 1 and word[0] == word[-1]:
    #         is_palindrome = True
    #     word = word[1:-1]

    # # while len(word) >= 1:
    # #     if 3 >= len(word) > 1 and word[0] == word[-1]:
    # #         is_palindrome = True
    # #     word = word[1:-1]

    # return is_palindrome


if __name__ == "__main__":
    word = ""
    print(is_palindrome_iterative(word))
