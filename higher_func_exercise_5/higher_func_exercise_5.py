"""Represent a small bilingual lexicon as a Python dictionary in the following fashion
 {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
  and use it to translate your Christmas cards from English into Swedish. Use the higher order function map()
  to write a function translate()
 that takes a list of English words and returns a list of Swedish words."""


def translate(english_word):
    lexicon = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    swedish_word = lexicon[english_word]
    return swedish_word

english_sentence = ["merry","christmas", "and", "happy", "new", "year"]

swedish_sentence = list(map(translate, english_sentence))
print(english_sentence,"\n", swedish_sentence)
