text = input()

# Setting a dictionary of the letters for replacement
library = {"é": "e", "ë": "e", "á": "a", "å": "aa", "œ": "oe", "æ": "ae"}


def normalize(name):
    for char in library.keys():
        # checking for ligatures and diacritic appearance, if exists in a string,
        # then replace it with corresponding value. Making letters to lowercase as the library keys are lowercase
        name = name.lower().replace(char, library[char])

    return name.title()


print(normalize(text))
