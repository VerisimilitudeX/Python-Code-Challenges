def sort_words(words):
    return sorted(words.split(), key=str.lower)

sort_words(input("Enter a string: "))