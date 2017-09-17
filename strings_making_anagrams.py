def number_needed(a, b):
    letter_dict = {}
    
    for letter in a:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
    for letter in b:
        letter_dict[letter] = letter_dict.get(letter, 0) - 1

    total = 0
    for value in letter_dict.itervalues():
        total += abs(value)
    return total

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
