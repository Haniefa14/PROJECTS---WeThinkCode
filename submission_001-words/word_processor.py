import string
import operator
from collections import Counter

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)
    
def convert_to_word_list(text):
    
    x = split(",.? ", text.lower())
    list_comprehension = [i.lower() for i in x if i not in " "] 

    return list_comprehension

def words_longer_than(length, text):
 
    word_len = []
    txt = convert_to_word_list(text)
    list1 = [x for x in txt if len(x) > length]
    return list1

def words_lengths_map(text):

    word = text
    w_len = word.translate(str.maketrans('', '',string.punctuation))
    new = w_len.split() 
    word_length = [len(words) for words in new]

    count_list = dict(Counter(word_length))
    sort_dict = count_list.items() #dict(sorted(count_list.items(), key=operator.itemgetter(1), reverse=True))
    sorted_dict = dict(sorted(sort_dict))
    #final_dict = dict(zip(count_list.values(), count_list.keys()))
    # length = list(set(word_length))
    #return word_length
    # new_list = []
    # [new_list.append(x) for x in length if x not in new_list]
    # return new_list
    return sorted_dict


    # for word in text.split():
    #     if len(word) not in x:
    #         x[len(word)] = 1
    #     else:
    #         x[len(word)] += 1
    # return (sorted([(k, v) for k, v in x.items()]))
    
def letters_count_map(text):

    letter_count = dict( (key, text.count(key)) for key in string.ascii_lowercase)
    return letter_count

def most_used_character(text):
    count_letters = letters_count_map(text)
    highest_value = max(count_letters, key=count_letters.get)
    return highest_value

if __name__ == "__main__":
    x = convert_to_word_list("These are indeed interesting, an obvious understatement, times. What say you?")
    print(x)
    words = words_longer_than(10, 'These are indeed interesting, an obvious understatement, times. What say you?')
    print(words)
    word_lengths = words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
    print(word_lengths)
    char_count = letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
    print(char_count)

    popular_char = most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
    print(popular_char)
