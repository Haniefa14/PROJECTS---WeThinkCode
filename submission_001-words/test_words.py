import unittest 
from io import StringIO

import word_processor


class MyTestCase(unittest.TestCase):
    def test_conversion_list(self):    
        result = word_processor.convert_to_word_list('Days are dark, but will my FRIENDS be there?')
        self.assertEqual(word_processor.convert_to_word_list('Days are dark, but will my FRIENDS be there?'),result)
        #self.assertEqual(word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?'),result)
    
    def test_word_length(self):
        result = word_processor.words_longer_than(5, 'Days are dark, but will my FRIENDS be there?')
        self.assertEqual(word_processor.words_longer_than(5, 'Days are dark, but will my FRIENDS be there?'), result)

    
    
    def test_words_map(self):
        result = word_processor.words_lengths_map('Days are dark, but will my FRIENDS be there?')
        self.assertEqual(word_processor.words_lengths_map('Days are dark, but will my FRIENDS be there?'),result)

    def test_letter_count(self):
        self.assertEqual(word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?'),{'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0})
        

    def test_used_char(self):
        
        self.assertEqual(word_processor.most_used_character(''), None)
        self.assertEqual(word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?'), 'e')
    

if __name__ == "__main__":
    unittest.main()