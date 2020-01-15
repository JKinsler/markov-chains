"""Generate Markov text from text files."""

from random import choice

import sys




def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    f = open(file_path, "r")
    text = f.read()

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text_list = text_string.split()

    index = 0
    while index < (len(text_list) - 2):

        # create a variable to hold the current chain key
        chain_key = (text_list[index], text_list[index+1])
        # create a variable to hold the dictionary value
        new_value = text_list[index+2]

        if chain_key not in chains:
            chains[chain_key] = []

        chains[chain_key].append(new_value)

        index = index + 1
    # your code goes here

    return chains


def get_new_word(key, chains):
    """Returns a new word as a random choice from the key's values. """
    values = chains[key]
    return choice(values)


def get_new_key(key, word):
    """Returns a new key based on the previous key and word. """
    return (key[1], word)


def make_text(chains):
    """Return text from chains."""
    key = choice(list(chains.keys()))

    words = []

    while key in chains:
        word = get_new_word(key, chains)
        words.append(word)
        key = get_new_key(key, word)

    return " ".join(words)


#input_path = "gettysburg.txt"
filename = sys.argv[1]   # first real argument

# Open the file and turn it into one long string
input_text = open_and_read_file(filename)
# print(input_text)
# print(type(input_text))

# Get a Markov chain
chains = make_chains(input_text)
# print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
