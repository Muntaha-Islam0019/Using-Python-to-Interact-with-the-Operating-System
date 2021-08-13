def character_frequency(filename):
    """Counts the frequency of character in the given file."""

    # Trying to open the file
    try:
        f = open(filename)
    except OSError:
        return None

    # Processing the file
    characters = {}
    for line in f:
        for char in  line:
            characters[char] = characters.get(char, 0) + 1
    f.close()

    return characters

