from super_fast_typing import choose_random_sentence, calc_accuracy, calculate_typing_speed


def test_choose_random_word():
    """Test choose_random_sentence method."""

    random_line = choose_random_sentence(file_name="words_words.txt")

    assert isinstance(random_line, str), f'Return type must be "str" but is {type(random_line)}.'


def test_calc_accuracy():
    """Test calc_accuracy method."""

    new = "He was the only member of the club who didn't like plum pudding."
    sentence = "He was the only member of the club who didn't like plum pudding."
    new_wrong = "He was the only members of the club who didn't like plums pudding."

    mistake1, word_count1 = calc_accuracy(new=new, sentence=sentence)

    assert isinstance(mistake1, int), f'Return type must be "int" but is {type(mistake1)}.'

    assert isinstance(word_count1, int), f'Return type must be "int" but is {type(word_count1)}.'

    assert mistake1 == 0, f'There must be 0 mistakes but found {mistake1}.'

    assert word_count1 == 13, f'There must be 13 words but found {word_count1}.'

    mistake2, _ = calc_accuracy(new=new_wrong, sentence=sentence)

    assert mistake2 == 2, f'There must be 2 mistakes but found {mistake2}.'


def test_calculate_typing_speed():
    """Method is used to test calculate_typing_speed."""

    typing_speed = calculate_typing_speed(correct_words=20, time=29.9)

    assert isinstance(typing_speed, int), f'Return type must be "int" but is {type(typing_speed)}.'

    assert typing_speed > 0, f'Result must be more than 0 but is {typing_speed}.'