# -*- coding: utf-8 -*-
"""
Tests for zantext functions.
"""
import unittest

from zantext import word, sentence


class TestZantextFunctions(unittest.TestCase):
    """ Tests for functions in the zantext module."""

    def test_word_creates_word_of_given_length(self):
        """When supplied with a length argument, the function word() should
        generate a word of the given length."""
        my_word = word(length=20)
        self.assertEqual(len(my_word), 20)
        for i in range(1, 26):
            my_word = word(length=i)
            self.assertEqual(len(my_word), i)

    def test_word_creates_word_no_longer_than_26_chars(self):
        """The function word() should generate words no longer than 26 chars.
        If supplied with a length argument greater than 26, it should generate
        words of length 3 to 10."""
        for i in range(26, 127):
            my_word = word(length=i)
            self.assertTrue(26 >= len(my_word) >= 3)

    def test_word_creates_word_based_on_absolute_value_of_length_argument(self):
        """The word() function should create words based on the absolute values
        of the length argument. eg. length=-4 == length=4"""
        for i in range(1, 26):
            i = -i
            my_word = word(length=i)
            self.assertEqual(len(my_word), abs(i))

    def test_word_creates_words_with_no_argument(self):
        """When no argument is given, word() should create words of length
        three to ten letters."""
        for i in range(55):
            my_word = word()
            self.assertTrue(3 <= len(my_word) <= 10)

    def test_sentence_creates_sentence_of_average_length_with_no_argument(self):
        """When given no argument, sentence() should generate sentences between
        three and ten words long."""
        for i in range(127):
            my_sentence = sentence()
            self.assertTrue(10 >= len(my_sentence.split()) >= 3)

    def test_sentence_creates_sentence_of_given_length(self):
        """The sentence() function should generate sentences with the number of
        words equal to the number given in the 'words' argument."""
        for i in range(1, 127):
            my_sentence = sentence(i)
            self.assertEqual(len(my_sentence.split()), i)


if __name__ == "__main__":
    unittest.main()
