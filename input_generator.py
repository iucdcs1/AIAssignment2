import random
import string
import nltk
from nltk.corpus import words

nltk.download('words')


def generate_real_word():
    word_list = [word for word in words.words() if 4 < len(word) < 15]
    return random.choice(word_list)


def create_and_save_words(start_position, n):
    for i in range(start_position + 1, start_position + 11):
        real_words = [generate_real_word().lower() for _ in range(n)]
        file_path = f'inputs/input{i}.txt'

        with open(file_path, 'w') as file:
            file.write('\n'.join(real_words))

        print(f'{len(real_words)} real words (15 > length > 4) saved to {file_path}')


if __name__ == "__main__":
    for x in range(2, 11):
        create_and_save_words((x - 2) * 10, x)
