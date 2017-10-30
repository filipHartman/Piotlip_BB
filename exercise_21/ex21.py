def char_freq(sentence):
    used_char = []
    chars_in_sentence = {}
    for char in sentence:
        if char not in used_char:

            count = 0
            count = count_number_of_char_in_sentence(count, char, sentence)
            chars_in_sentence[char] = count
            used_char.append(char)

    display = []
    for char in chars_in_sentence:
        char_info = '{} ----->  {}'.format(char, chars_in_sentence[char])
        display.append(char_info)
    return '\n'.join(display)


def count_number_of_char_in_sentence(count, char, sentence):
    for letter in sentence:
        if check_letter_equal_to_char(letter, char):
            count += 1
    return count


def check_letter_equal_to_char(letter, char):
    if letter == char:
        return True
    return False


sentence = 'abbabcbdbabdbdbabababcbcbab'
print(char_freq(sentence))
