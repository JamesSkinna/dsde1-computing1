'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containing the first and the last element
# of "the_list". 
def first_and_last(the_list):
    new_list = list()
    new_list.append(the_list[0])
    new_list.append(the_list[-1])
    return new_list


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    the_list = [1, 2, 3, 4, 5]
    beginning = 1
    end = 4
    end_of_list = len(the_list)
    if (end < beginning) or (beginning < 0) or (end > end_of_list):  
        raise ValueError
    else: 
        new_list = the_list[beginning: end]
        new_list = new_list.reverse()
    return new_list


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    repeated_value = the_list[index]
    for i in range(0, 2):
        the_list.insert(index, repeated_value)
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    palindrome_test = ""
    word = word.lower()
    for letter in word:
        palindrome_test = letter + palindrome_test 
    return palindrome_test == word

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    sentence = sentence.lower()
    new_sentence = ""
    palindromic_sentence = ""
    for letter in sentence:
        if ord(letter) <= 120 and ord(letter) >= 97:
            new_sentence = new_sentence + letter
            palindromic_sentence = letter + palindromic_sentence
    return new_sentence == palindromic_sentence

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    sentence1 = sentence1.strip()
    sentence2 = sentence2.strip()
    if sentence1[0].isupper() and sentence2[0].isupper():
        if (sentence1[-1] == "." or sentence1[-1] == "?" or sentence1[-1] == "!") and (sentence2[-1] == "." or sentence2[-1] == "?" or sentence2[-1] == "!"):
            new_sentence = sentence1 + " " + sentence2
        else: raise ValueError
    else: raise ValueError       
    return new_sentence


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    return key in dictionary

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    is_stored = False
    for the_keys in dictionary:
        if dictionary[the_keys] == value:
            is_stored = True
    return is_stored

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary1.update(dictionary2)
    return dictionary1

"""
def main():
    print(palindrome_word("test"))
    print(palindrome_word("hannah"))

if __name__ == "__main__":
    main() 
"""