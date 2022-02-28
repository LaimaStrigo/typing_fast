import random
from time import time
from typing import Tuple

file_name = "words_words.txt"


def choose_random_sentence(file_name: str) -> str:
    """Chooses random sentence from file.

    :param file_name: name of the file from which import sentences
    :return returns random sentence
    """

    with open(file_name, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
    return random_line


def calc_accuracy(new: str, sentence: str) -> Tuple[int, int]:
    """Method is used to count written words and mistakes.

    :param new: sentence from the input
    :param sentence: random generated sentence
    :return count of the mistakes, count of words in sentence
    """

    mistake = 0
    word_count = 0
    new = new.replace("\n", "")
    split_new = new.split(" ")

    for position, word in enumerate(sentence.split(" ")):
        word_count += 1
        if word != split_new[position]:
            mistake += 1
    return mistake, word_count


def calculate_typing_speed(correct_words: int, time: float) -> float:
    """Method is used to calculate the typing speed.

    :param correct_words: count of the correctly typed words
    :param time: time spent on typing (seconds)
    :return calculated typing speed (wpm)
    """

    typing_speed = (correct_words * 60) / time

    return round(typing_speed)


if __name__ == "__main__":

    new_sentence = choose_random_sentence(file_name=file_name)

    print('***Welcome to super mega fast printing training program!!!***\n'
          'Here you will get randomly generated sentence: \n')
    print(new_sentence)
    input('Press ENTER when you will be ready...')
    print()

    start_time = time()
    sentence = input()
    end_time = time()

    mistakes, words = calc_accuracy(new=new_sentence, sentence=sentence)
    time = end_time - start_time
    correct_words = words - mistakes
    typing_speed = calculate_typing_speed(correct_words=correct_words, time=time)

    print(f"Number of the mistakes: {mistakes}. Total correct words : {correct_words}.")
    print(f"Accuracy: {(1 - (mistakes / words)) * 100} %.")
    print(f"Time spent on typing: {round(time, 2)} seconds.", )
    print(f"Your super fast typing speed is: {typing_speed} wpm.")
