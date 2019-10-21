"""

A simple program that plays Shannon's Game.
Students are to complete FrequencyList's methods and then use this class to decide what guesses should be made while playing Shannon's Shannon's Game.


Author:Shivin Gaba
Date:
"""
import doctest
import sys
import time
import re
from unicodedata import category


DEFAULT_CORPUS = 'corpus.txt'


class FrequencyNode:
    """
    Stores a letter:frequency pair.
    We use this class as a constituent part of a gerneric graph, such as a linked list

    >>> test = FrequencyNode('c', 2)
    >>> test.letter
    'c'
    >>> test.frequency
    2
    >>> test
    FrequencyNode('c', 2)
    """

    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        # The next FrequencyNode object when stored as part of a linked list
        self.next_node = None

    def __repr__(self):
        return 'FrequencyNode({}, {})'.format(repr(self.letter), repr(self.frequency))




class FrequencyList:
    """Stores a collection of FrequencyNode objects as a linked list."""

    def __init__(self):
        """ Creates an empty FrequencyList """
        self.head = None

    def add(self, letter, frequency=1):
        """
        If the given `letter` is already in the list,
          the given frequency is added to its frequency.
        Otherwise adds the given letter:frequency combination as a FrequencyNode object
        to the end of the list.

        There is an extra exercise that students can do if they want related to keeping the list in order,
        even if you do not complete that task can you think of why this could help improve performance when the
        list is used in Shannon's Game?

        

        >>> test = FrequencyList()
        >>> test.add('a', 3)
        >>> test
        FrequencyNode List -> FrequencyNode('a', 3) -> None
        >>> test.add('b', 2)
        >>> test
        FrequencyNode List -> FrequencyNode('a', 3) -> FrequencyNode('b', 2) -> None
        >>> test.add('b', 1)
        >>> test
        FrequencyNode List -> FrequencyNode('a', 3) -> FrequencyNode('b', 3) -> None
        """
   
        current = self.head
        previous = None
        if self.head == None: 
            self.head = FrequencyNode(letter, frequency)
        else:
            while current != None:
                if current.letter == letter: 
                    current.frequency += frequency   
                    return
                else:
                    previous = current
                    current = current.next_node
            previous.next_node = FrequencyNode(letter, frequency)
         

    def remove(self, letter):
        """
        Removes the FrequencyNode object with the given `letter` from the list.
        Does nothing if `letter` is not in the list.

        NOTE: YOU MUST write some doctests for the remove method here!
        >>> f = FrequencyList()
        >>> f.add('a', 3)
        >>> f.add('b', 2)
        >>> f.add('c', 3)
        >>> f
        FrequencyNode List -> FrequencyNode('a', 3) -> FrequencyNode('b', 2) -> FrequencyNode('c', 3) -> None
        """
       
        current = self.head 
        previous = None        
        if current == None: 
            return self.head 
        if previous == None and current.letter == letter:# in this case we just need to set the new value for the head
            self.head = current.next_node 
        else:
            found = False 
            while current != None and not found: 
                if current.letter == letter:
                    previous.next_node = current.next_node # changing the pointer here from 
                        #previous to point the current and that current points to the nect of it.
                    found = True 
                else:
                    previous = current 
                    current = current.next_node

    def find(self, letter):
        """
        Returns the FrequencyNode object for the given `letter` in the list, or
        None if the `letter` doesn't appear in the list.

        YOU MUST write more doctests for this method!

        >>> f = FrequencyList()
        >>> f.add('a', 3)
        >>> f.find('a')
        FrequencyNode('a', 3)
        >>> f.find('b')

        """
       
        current = self.head 
        while current != None:
            if current.letter == letter:
                return current 
            else:
                current = current.next_node 
        

    def __contains__(self, item):
        """ Returns True if item is in this FrequencyList
        Remember self.find(item) will return the index of the item
        if the item is in the list otherwise it returns None.

        >>> f = FrequencyList()
        >>> f.add('a', 3)
        >>> 'a' in f
        True
        >>> 'b' in f
        False

        """
        return self.find(item) is not None

    def __len__(self):
        """ Returns the length of the FrequncyList, zero if empty
        YOU MUST write some more doctests here.
        >>> f = FrequencyList()
        >>> f.add('a', 3)
        >>> len(f)
        1
        >>> f.add('b', 1)
        >>> len(f)
        2
        >>> f.add('c', 1)
        >>> len(f)
        3
        """
        
        length = 0 
        current = self.head 
        if current == None: 
            return 0 
        else:
            found = False
            while current != None:
                current = current.next_node
                length += 1
            return length 
       

    def __repr__(self):
        """ Returns a string representation of the list in the form
        FrequencyNode List -> FrequencyNode('a', 2) -> FrequencyNode('b', 10) ... -> None
        """
        current = self.head
        result = 'FrequencyNode List -> '
        while current is not None:
            result += repr(current) + ' -> '
            current = current.next_node
        result += 'None'
        return result





def get_prediction_list(corpus, last):
    """
    Returns a Python list of all instances of single characters in 'corpus' that
    immediately follow 'last' (including duplicates). The characters should be
    in that same order as they appear in the corpus

    The 'corpus' and 'last' should be all lowercase characters.

    Duplicates are included - see the doctests below.

    YOU MUST write more doctests!

    >>> get_prediction_list('lazy languid line', 'la')
    ['z', 'n']
    >>> get_prediction_list('pitter patter batton', 'tt')
    ['e', 'e', 'o']
    >>> get_prediction_list('pitter pattor batt', 'tt')
    ['e', 'o']
    >>> get_prediction_list('pitter pattor batt', 'er')
    [' ']
    """
     
    
    new = []
    for i in range(0, len(corpus)): 
        if last in corpus[i: i + 2]: 
            letter = corpus[i+2:i+3] 
            if letter != '':
                new.append(letter) 
    return new 
            
    


def count_frequencies(items):
    """
    Counts the frequencies of each element in `items` and returns a
    FrequencyList of FrequencyNode objects containing the element and frequency.
    The items in the returned LinkedList should be in the same order as they appear in the
    items list (they don't need to be sorted by frequency).

    NOTE: You will need to write some more doctests here!

    >>> count_frequencies(['e', 'e', 'o'])
    FrequencyNode List -> FrequencyNode('e', 2) -> FrequencyNode('o', 1) -> None
    >>> count_frequencies(['j', 'i', 'k', 'k', 'k', 'i'])
    FrequencyNode List -> FrequencyNode('j', 1) -> FrequencyNode('i', 2) -> FrequencyNode('k', 3) -> None
    >>> freqs = count_frequencies(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'c', 'b'])
    >>> # Print in order
    >>> current = freqs.head
    >>> while current is not None:
    ...    print(current)
    ...    current = current.next_node
    FrequencyNode('a', 1)
    FrequencyNode('b', 2)
    FrequencyNode('c', 2)
    FrequencyNode('d', 1)
    FrequencyNode('e', 1)
    FrequencyNode('f', 1)
    FrequencyNode('g', 1)
    """
  
    freq_list = FrequencyList() 
    for letter in items:
        freq_list.add(letter, frequency=1)
    return freq_list 
        
    


def select_next_guess(possibles):
    """
    Removes and returns the letter with the highest frequency from the
    'possibles' FrequencyList.
    If more than one letter has the highest frequency then the first
    letter in the list with that frequency is returned.
    Returns None if there are no more guesses.

    YOU MUST write some more doctests!

    >>> p = FrequencyList()
    >>> p.add('a', 2)
    >>> p.add('b', 4)
    >>> p.add('c', 1)
    >>> p.add('d', 4)
    >>> p
    FrequencyNode List -> FrequencyNode('a', 2) -> FrequencyNode('b', 4) -> FrequencyNode('c', 1) -> FrequencyNode('d', 4) -> None
    >>> select_next_guess(p)
    'b'
    """
    
    calling = count_frequencies(possibles)
    return calling 
        
   




###############################################################################
#################### DO NOT MODIFY ANYTHING INSIDE THE BLOCK BELOW ############
################# There is some code below this block you should read #########
###############################################################################

def fallback_guesses(possibles):
    """
    Returns all characters from a--z, and some punctuation that don't appear in
    `possibles`.
    """
    all_fallbacks = [chr(c) for c in range(ord('a'), ord('z') + 1)] + \
                    [' ', ',', '.', "'", '"', ';', '?', '!']
    fallbacks = [x for x in all_fallbacks if x not in possibles]
    return fallbacks


def format_document(doc):
    """
    Re-formats `doc` by collapsing all whitespace characters into a space and
    stripping all characters that aren't letters or punctuation.
    """
    # http://www.unicode.org/reports/tr44/#General_Category_Values
    allowed_categories = ('Lu', 'Ll', 'Lo', 'Po', 'Zs')
    # d = unicode(d, 'utf-8')
    # d = str(d, 'utf-8')
    # Collapse whitespace
    doc = re.compile(r'\s+', re.UNICODE).sub(' ', doc)
    doc = u''.join([c.lower() for c in doc if category(c) in allowed_categories])
    # Disable the encode to properly process a unicode corpus
    return doc


def confirm(prompt):
    """
    Asks the user to confirm a yes/no question.
    Returns True/False based on their answer.
    """
    answer = ' '
    while len(answer) == 0 or answer[0].lower() not in ('y', 'n'):
        answer = input(prompt + ' (y/n) ')
    return answer[0].lower() == 'y'


def check_guess(next_char, guess):
    """
    Returns True if `guess` matches `next_char`, or asks the user if
    `next_char` is None.
    """
    if next_char is not None:
        return next_char == guess
    else:
        return confirm(" '{}'?".format(guess))


def check_guesses(next_char, guesses):
    """
    Runs through `guesses` to check against `next_char` (or asks the user if
    `next_char` is None).
    If a correct guess is found, (guess, count) is returned; otherwise
    (None, count) is returned. Where `count` is the number of guesses
    attempted.
    """
    guess = select_next_guess(guesses)
    guess_count = 0
    while guess is not None:
        guess_count += 1
        if check_guess(next_char, guess):
            return guess, guess_count
        guess = select_next_guess(guesses)
    # Wasn't able to find a guess
    return None, guess_count


def check_fallback_guesses(next_char, guesses):
    """
    Runs through 'guesses' to check against 'next_char' (or asks the user if
    'next_char' is None).
    If a correct guess is found, (guess, count) is returned; otherwise
    (None, count) is returned. Where 'count' is the number of guesses
    attempted.
    """
    guess_count = 0
    for guess in guesses:
        guess_count += 1
        if check_guess(next_char, guess):
            return guess, guess_count

    # If that failed, we're screwed!
    print('Exhaused all fallbacks! Failed to guess phrase.')
    sys.exit(1)


def get_guesses_list(corpus, progress):
    """ Returns the frequency list of guesses
    Guesses should appear in the same order in the input file
    """
    pair = progress[-2:]  #.lower()
    possibles = get_prediction_list(corpus, pair)
    if possibles is None:
        sys.stderr.write('get_prediction_list has not been ' +
                         'implemented!\n')
        sys.exit(1)

    guesses = count_frequencies(possibles)
    if guesses is None:
        sys.stderr.write('count_frequencies has not been implemented!\n')
        sys.exit(1)
    return guesses


def find_next_char(corpus, phrase, progress, is_auto):
    """ Keeps guessing until the right character is chosen.
    With crash and burn if can't guess it.
    """
    guesses = get_guesses_list(corpus, progress)
    fallbacks = fallback_guesses(guesses)
    # Figure out what the next character to guess is
    next_char = phrase[len(progress)].lower() if is_auto else None
    # Try to guess it from the corpus
    (guess, char_guess_count) = check_guesses(next_char, guesses)
    # If guessing from the corpus failed, try guessing from the fallbacks
    if guess is None:
        print('Exhausted all guesses from the corpus! Just guessing...')
        (guess, fb_count) = check_fallback_guesses(next_char, fallbacks)
        char_guess_count += fb_count
    return guess, char_guess_count


def play_game(corpus, phrase, phrase_len=0):
    """
    Plays the game.
      'corpus' is the complete corpus to use for finding guesses.
      'phrase' is the phrase to match, or part of the phrase.
      'phrase_len' is the total length of the phrase or 0 for auto mode
    If 'phrase_len' is zero, then the game is played automatically and
    the phrase is treated as the whole phrase. Otherwise the phrase is
    the start of the phrase and the function will ask the user whether
    or not it's guesses are correct - and keep going until phrase_len
    characters have been guessed correctly.

    Given phrase_len is 0 by default leaving out phrase_len from
    calls will auto-run, eg, play_game(corpus, 'eggs') will auto-run

    Returns the total number of guesses taken and the total time taken
    If in interactive mode the time taken value will be 0.
    """
    is_auto = phrase_len == 0
    if is_auto:
        phrase_len = len(phrase)
    progress = phrase[0:2]
    total_guesses = 0

    start = time.perf_counter()
    gap_line = '_' * (phrase_len - len(progress))
    print('{}{}  (0)'.format(progress, gap_line))
    while len(progress) != phrase_len:
        next_char, guesses = find_next_char(corpus, phrase, progress, is_auto)
        total_guesses += guesses
        progress += next_char
        gap_line = '_' * (phrase_len - len(progress))
        print('{}{}  ({})'.format(progress, gap_line, guesses))
    end = time.perf_counter()

    print(' Solved it in {} guesses!'.format(total_guesses))
    # return zero if in interactive mode
    time_taken = end - start if is_auto else 0
    return total_guesses, time_taken


def load_corpus_and_play(corpus_filename, phrase, length=0):
    """ Loads the corpus file and plays the game with the given setttings
    >>> filename = 'the-yellow-wall-paper.txt'
    >>> phrase = 'document test phrase'
    >>> load_corpus_and_play(filename, phrase)  # doctest: +ELLIPSIS
    Loading corpus... the-yellow-wall-paper.txt
    Corpus loaded. (49812 characters)
    do__________________  (0)
    doc_________________  (10)
    Exhausted all guesses from the corpus! Just guessing...
    docu________________  (21)
    Exhausted all guesses from the corpus! Just guessing...
    docum_______________  (18)
    docume______________  (3)
    documen_____________  (2)
    document____________  (3)
    document ___________  (1)
    document t__________  (2)
    document te_________  (4)
    document tes________  (5)
    document test_______  (3)
    document test ______  (1)
    document test p_____  (15)
    document test ph____  (7)
    document test phr___  (3)
    document test phra__  (3)
    document test phras_  (12)
    document test phrase  (2)
     Solved it in 115 guesses!
    ...
    """
    with open(corpus_filename, encoding='utf-8') as infile:
        print('Loading corpus... ' + corpus_filename)
        corpus = format_document(infile.read())
        print('Corpus loaded. ({} characters)'.format(len(corpus)))
        _, time_taken = play_game(corpus, phrase, length)
        if length == 0:
            print('Took {:0.6f} seconds'.format(time_taken))


###############################################################################
#################### DO NOT MODIFY ANYTHING INSIDE THE BLOCK ABOVE ############
###############################################################################




################### Your Testing Code Goes in here ############################

def run_time_trials():
    """ A good place to write code for time trials.
    We have given you some example code to get you started.
    Make sure you use this docstring to explain your code and that
    you write comments in your code to help explain the process.
    """
    corpus_filename = 'war-and-peace.txt'  # try others if you want
    with open(corpus_filename, encoding='utf-8') as infile:
        print('Loading corpus ... ' + corpus_filename)
        full_corpus = format_document(infile.read())
    results = []
    phrase = 'your test phrase should go here'
    # we go up to 50000 in steps of 2000 for a start
    # you may want to go all the way to the lenght of the corpus
    # to see what happens.
    for size in range(1000, 50000, 2000):
        slice_of_corpus = full_corpus[0:size]  # then try [0:2000] etc
        num_guesses, time_taken = play_game(slice_of_corpus, phrase)  # play with autorun
        print('With corpus size {:4} time taken = {}'.format(size, time_taken))
        results.append((size, num_guesses, time_taken))
    print('{:>6}  {:^12} {:^10}'.format('size', 'num_guesses', 'time_taken'))
    for size, num_guesses, time_taken in results:
        print('{:6}  {:^12}  {:^10.4f}'.format(size, num_guesses, time_taken))

    # As the corpus size increases the number of guesses generally falls
    # but why does the time increase?



def run_some_trials():
    """ Play some games with various test phrases and settings """
    # play game using whatever you like
    # maybe put an input statement here
    # so you can enter the corpus
    # and settings
    # or just run various games with various settings

    # MAKE SURE you test with various phrases!
    test_phrases = ["is it weird to have  two spaces in here?",
                    'dead war',
                    # 'Extreme emotional experiment',
                    ]
    test_files = [DEFAULT_CORPUS,
                  # Some other file names
                  # 'the-yellow-wall-paper.txt',
                  # 'hamlet.txt',
                  # 'le-rire.txt',
                  # 'war-of-the-worlds.txt',
                  # 'ulysses.txt',
                  # 'war-and-peace.txt'
                  ]

    #Uncomment the block below to run trials based on the lists of phrases and files above
    for test_phrase in test_phrases:
        for corpus_filename in test_files:
            phrase_length = 0  # for auto-run
            load_corpus_and_play(corpus_filename, test_phrase, phrase_length)
            print('\n' * 3)

    # check out https://www.gutenberg.org/ for more free books!



def test():
    """ Runs doctests and other trials"""

    # Doctests
    # -----------------
    # Uncomment various doctest runs to check each method/function
    # MAKE sure your submitted code doesn't run tests - we will do this.
    # MAKE SURE you add some doctests of your own to the docstrings

    doctest.run_docstring_examples(FrequencyNode, globs=None)
    doctest.run_docstring_examples(FrequencyList.add, globs = None)
    doctest.run_docstring_examples(FrequencyList.remove, globs = None)
    doctest.run_docstring_examples(FrequencyList.find, globs = None)

    doctest.run_docstring_examples(get_prediction_list, globs = None)
    doctest.run_docstring_examples(count_frequencies, globs = None)
    doctest.run_docstring_examples(select_next_guess, globs = None)


    # Uncomment the line below to run all doctests - this is helpful before you submit
    # doctest.testmod()


    # Running trials
    # -----------------
    # Uncomment the call to run_some_trials below to run
    # whatever trials you have setup in that function
    # IMPORTANT: comment out the run_some_trials() line below
    # before you submit your code
    # run_some_trials()

    # Time trials
    # -----------------
    # Running time trials will give you a feel for how the speed
    # is affected by the corpus size
    # run_time_trials()

    # interactive trial
    # -----------------
    # see how long the program takes to guess 'bat man'
    # it will get the first two characters and start asking you
    # if it has the third character correct etc...
    # load_corpus_and_play('le-rire.txt', 'ba', 7)



################# End of Testing Code ########################################





def main():
    """ Put your calls to testing code here.
    The quiz server will not run this function.
    It will test directly
    """
    test()


# run this code if not being imported
if __name__ == '__main__':
    main()
    # don't add any code here

