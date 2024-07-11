""" Copyright 2017, Dimitrios Effrosynidis, All rights reserved. """

import re
from nltk.corpus import wordnet
import inflect


def replace_URL(text):
    # Replacing urls with the string "url"
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','url',text)
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text

def replace_AtUser(text):
    # Replacing tagging of other users in a tweet (@User) -> (atUser)
    text = re.sub('@[^\s]+','atUser',text)
    return text

def remove_hashtags(text):
    # Removing hashtags
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text

def replace_numbers(text):
    # Replaces integers to string text
    # For example, 1 -> One
    # This would allow for keeping relevant information and avoiding removing critical information
    
    def convert_numbers_to_words(match):
        number = match.group(0)
        p = inflect.engine()
        return p.number_to_words(number)
    
    text_with_words = re.sub(r'\b\d+\b', convert_numbers_to_words, text)

    # Below complete
    # text = ''.join([i for i in text if not i.isdigit()])         
    return text_with_words

# completely removes text
def remove_numbers(text):
    text = ''.join([i for i in text if not i.isdigit()])         
    return text


def replaceMultiExclamationMark(text):
    # Tag multi-exclamation marks
    text = re.sub(r"(\!)\1+", ' multiExclamation ', text)
    return text

def replaceMultiQuestionMark(text):
    # Tag multi-question marks
    text = re.sub(r"(\?)\1+", ' multiQuestion ', text)
    return text

def replaceMultiStopMark(text):
    # Tag multi-full-stops
    text = re.sub(r"(\.)\1+", ' multiStop ', text)
    return text

def countMultiExclamationMarks(text):
    # Count number of excalmation marks
    return len(re.findall(r"(\!)\1+", text))

def countMultiQuestionMarks(text):
    # Count number of question marks
    return len(re.findall(r"(\?)\1+", text))

def countMultiStopMarks(text):
    # Count number of full-stops
    return len(re.findall(r"(\.)\1+", text))

def countElongated(text):
    """ Input: a text, Output: how many words are elongated """
    regex = re.compile(r"(.)\1{2}")
    return len([word for word in text.split() if regex.search(word)])

def countAllCaps(text):
    """ Input: a text, Output: how many words are all caps """
    return len(re.findall("[A-Z0-9]{3,}", text))


# E.g. Can't -> cannot
contraction_patterns = [ (r'won\'t', 'will not'), (r'can\'t', 'cannot'), (r'i\'m', 'i am'), (r'ain\'t', 'is not'), (r'(\w+)\'ll', '\g<1> will'), (r'(\w+)n\'t', '\g<1> not'),
                         (r'(\w+)\'ve', '\g<1> have'), (r'(\w+)\'s', '\g<1> is'), (r'(\w+)\'re', '\g<1> are'), (r'(\w+)\'d', '\g<1> would'), (r'&', 'and'), (r'dammit', 'damn it'), (r'dont', 'do not'), (r'wont', 'will not') ]
def replace_contraction(text):
    patterns = [(re.compile(regex), repl) for (regex, repl) in contraction_patterns]
    for (pattern, repl) in patterns:
        (text, count) = re.subn(pattern, repl, text)
    return text

def replace_elongated(word):
    # E.g. Hellooooooo -> Hello

    repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
    repl = r'\1\2\3'
    if wordnet.synsets(word):
        return word
    repl_word = repeat_regexp.sub(repl, word)
    if repl_word != word:      
        return replaceElongated(repl_word)
    else:       
        return repl_word

def remove_emojis(text):
    """ Removes emoticons from text """
    text = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', '', text)
    return text

def count_emojis(text):
    """ Input: a text, Output: how many emoticons """
    return len(re.findall(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', text))



# TO-DO

# Find a way to replace spelling mistakes in tweets
# Look into more variety of emoticons that can be replaced or removed from the text



