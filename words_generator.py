from random import randint

alphabet = 'ёйцукенгшщзхъэждлорпавыфячсмитьбю'

words = ''
for i in range(1_000_000):
    words += ''.join([alphabet[randint(0, len(alphabet) - 1)] for _ in range(19)]) + '\n'

open('random_words.txt', 'w', encoding='UTF-8').write(words[:-1])

