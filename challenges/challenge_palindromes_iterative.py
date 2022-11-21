def is_palindrome_iterative(word):
    if len(word) == 0 or word[0] != word[-1]:
        return False
    if len(word) == 1:
        return True

    word = word.lower()
    ind = 0
    ind_max = len(word) - 1
    for ind in range(len(word)):
        if 2 >= ind_max - ind >= 1 and word[ind] == word[ind_max]:
            return True
        ind_max -= 1

    return False


if __name__ == "__main__":
    WORDS = [
        "ala",
        "ama",
        "anã",
        "anilina",
        "arara",
        "ata",
        "ele",
        "esse",
        "mamam",
        "matam",
        "metem",
        "mirim",
        "oco",
        "omissíssimo",
        "osso",
        "ovo",
        "radar",
        "raiar",
        "ralar",
        "reger",
        "reler",
        "reter",
        "rever",
        "reviver",
        "rir",
        "rodador",
        "sacas",
        "saias",
        "salas",
        "socos",
        "sós",
        "berinjela",
        "",
        "j",
    ]
    for word in WORDS:
        print(
            f"a palvra {word} é um palindromo? {is_palindrome_iterative(word)}"
        )
