def reverse(sentence):
    reversed_sentence = []
    for letter in sentence:
        reversed_sentence.insert(0, letter)
    return ''.join(reversed_sentence)

sentence = 'Ala ma kota, a kot ma wściekliznę'

print(reverse(sentence))
