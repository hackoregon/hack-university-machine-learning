#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ^-- This allows unicode characters to be copypastad from the web below
r"""Compiled regular expressions for tokenization and parsing

>>> list(m.group() for m in CRE_TOKEN.finditer("I'm sure \"Smiths'\" and \".net\" are easies; you?"))
["I'm", 'sure', '"', 'Smiths', '\'"', 'and', '"', '.', 'net', '"', 'are', 'easies', ';', 'you', '?']

 RE_YEAR
  >>> re.compile(RE_YEAR).findall("In '1970' and 2000, or 2015 '27 78 1886 with $1980 in my pocket")
  ['1970', '2000', '2015', '27', '78', '1980']
  >>> doc = r"In '1970-2000\1', 2015/16, and 27, many not-so-wealthy people's banks had $1980 more than Gates' or Jobs'."
  >>> [((s, LIST_RE_TOKEN_NAMED[i].lower()[3:]) for i, s in enumerate(groups) if s).next() for groups in re.compile(RE_TOKEN_NAMED).findall(doc)]
  [('In', 'unhyphenated_contracted_alpha'), ("'", 'nonword'), ('1970', 'year'), ('-', 'nonword'), ('2000', 'year'), ('\\', 'nonword'),
   ('1', 'float'), ("',", 'nonword'), ('2015', 'year'), ('/', 'nonword'), ('16', 'year'), (',', 'nonword'), ('and', 'unhyphenated_contracted_alpha'),
   ('27', 'year'), (',', 'nonword'), ('many', 'unhyphenated_contracted_alpha'), ('not-so', 'hyphenated_alpha'), ('-', 'nonword'),
   ('wealthy', 'unhyphenated_contracted_alpha'), ("people's", 'unhyphenated_contracted_alpha'), ('banks', 'unhyphenated_contracted_alpha'),
   ('had', 'unhyphenated_contracted_alpha'), ('$1980', 'usd'), ('more', 'unhyphenated_contracted_alpha'), ('than', 'unhyphenated_contracted_alpha'),
   ('Gates', 'unhyphenated_contracted_alpha'), ("'", 'nonword'), ('or', 'unhyphenated_contracted_alpha'), ('Jobs', 'unhyphenated_contracted_alpha'),
   ("'.", 'nonword')]

RE_WORD_BASIC
  Disallows underscores,  hyphens, leading numerals, and leading punctuation (except dot e.g. ".Net").
  Trailing digits and mixed case accepted. Word break (\b) not required.
  >>> tough_words = "1on1 2_on_2\r19+2-1=4^2+2**2\tTitle9\n.Net SuperCalaFragalisticExpiAladozious Titles and a I"
  >>> ' '.join(m.group() for m in re.finditer(RE_WORD_BASIC, tough_words))
  'on1 on Title9 .Net SuperCalaFragalisticExpiAladozious Titles and a I'

RE_WORD_LIBERAL
  Allows underscores, hyphens, digits anywhere (trailing or leading).
  >>> ' '.join(iter_finds(RE_WORD_LIBERAL, tough_words))
  '1on1 2_on_2 19 2-1 4 2 2 2 Title9 .Net SuperCalaFragalisticExpiAladozious Titles and a I'

RE_WORD_ALGEBRA
  Underscores, hyphens, digits, and math operators allowed anywhere, but no whitespace
  >>> ' '.join(iter_finds(RE_WORD_ALGEBRA, tough_words))
  '1on1 2_on_2 19+2-1=4^2+2**2 Title9 .Net SuperCalaFragalisticExpiAladozious Titles and a I'

RE_WORD_UNDERSCORED
  2 to 3 "words" joined by internal underscores is an underscored word
  If external_underscores aren't matched by some preceding regex
  >>> compound_words = "Not-so-crazy words _underscored_externally_ and_internally and-very-long-up-to-64"
  >>> ' '.join(iter_finds(RE_WORD_UNDERSCORED, compound_words))
  'underscored_externally and_internally'

RE_PHRASE_UNDERSCORED
  4 to 64 "words" joined by internal underscores is a "PHRASE", like the title of a book or file
  >>> ' '.join(iter_finds(RE_PHRASE_UNDERSCORED, compound_words))
  ''

Only CAMEL_LIBERAL can start or end with an ACRONymn
But RE_ACRONYM only allows 5-char long acronyms, max. But the 6th can be the start of a title-case word.
RE_CAMEL_NORMAL
  >>> [re.match(RE_CAMEL_NORMAL, s).group() for s in ['redRising', 'GoldenChildMorningStar']]
  ['redRising', 'GoldenChildMorningStar']
  >>> list(re.finditer(RE_CAMEL, 'Morning5star Investing'))
  []
  >>> list(m.group() for m in re.finditer(RE_CAMEL_NORMAL, 'EPR: AlbertEinstein BorisPodolsky And NathanRosen'))
  ['AlbertEinstein', 'BorisPodolsky', 'NathanRosen']

RE_CAMEL_LIBERAL, RE_CAMEL_LIBERAL_B
  >>> list(m.group() for m in re.finditer(RE_CAMEL_LIBERAL, 'EinsteinPR: Einstein bPodolskyNRA NOTNRAPodolsky'))
  ['EinsteinPR', 'bPodolskyNRA', 'NOTNRAPodolsky']
  >>> list(m.group() for m in re.finditer(RE_CAMEL_LIBERAL_B, 'EinsteinPR: Einstein bPodolskyNRA NOTNRAPodolsky'))
  ['EinsteinPR', 'bPodolskyNRA', 'NOTNRAPodolsky']
  >>> [groups[0] for groups in re.findall(RE_CAMEL_LIBERAL_B, 'EinsteinPR: Einstein bPodolskyNRA NOTNRAPodolsky')]
  ['EinsteinPR', 'bPodolskyNRA', 'NOTNRAPodolsky']

FIXME: too narrow! probably because of all the \b checks
RE_DOTTED_ACRONYM_B
  >>> list((m.group() if m else None) for m in re.finditer(RE_DOTTED_ACRONYM_B, 'U.S., U.S.A., A., and B.'))
  ['U.', 'U.S.']

RE_ACRONYM, RE_ACRONYM_B
  >>> re.findall(RE_ACRONYM, 'Hello ACRNYM cANDid ATe')
  ['ACRNYM', 'AND', 'AT']
  >>> re.findall(RE_ACRONYM_B, 'Hello ACRNYM cANDid ATe')
  ['ACRNYM']

RE_CAMEL_BASIC_B, RE_CAMEL_NORMAL_B, RE_CAMEL_LIBERAL_B
  >>> [getattr(try_next(re.finditer(s, "Hello CamelACRONYM cANDid ATe")), 'group', bool)()
  ...  for s in (RE_CAMEL_BASIC_B, RE_CAMEL_NORMAL_B, RE_CAMEL_LIBERAL_B)]
  [False, False, 'CamelACRONYM']
"""

import re
import string

MAX_CHR = MAX_CHAR = chr(127)
APOSTROPHE_CHARS = "'`’"
UNPRINTABLE = ''.join(set(chr(i) for i in range(128)) - set(string.printable))
string.unprintable = UNPRINTABLE  # monkey patch so import string from this module if you want this!


def iter_finds(regex_obj, s):
    """Generate all matches found within a string for a regex and yield each match as a string"""
    if isinstance(regex_obj, basestring):
        for m in re.finditer(regex_obj, s):
            yield m.group()
    else:
        for m in regex_obj.finditer(s):
            yield m.group()


def try_next(it, default=None):
    try:
        return it.next()
    except StopIteration:
        return default


def try_get(obj, idx, default=None):
    try:
        return obj.__getitem__(idx)
    except IndexError:
        return default


def wrap(s, prefix=r'\b', suffix=r'\b', grouper='()'):
    r"""Wrap a string (tyically a regex) with a prefix and suffix (usually a nonconuming word break)

    Arguments:
      prefix, suffix (str): strings to append to the front and back of the provided string
      grouper (2-len str or 2-tuple): characters or strings to separate prefix and suffix from the middle

    >>> wrap(r'\w*')
    '\\b(\\w*)\\b'
    >>> wrap(r'middle', prefix=None)
    '(middle)\\b'
    """
    return (prefix or '') + try_get(grouper, 0, '') + (s or '') + try_get(grouper, 1, try_get(grouper, 0, '')) + (suffix or '')


RE_BAD_FILENAME = '[{}]'.format(re.escape(string.punctuation + string.unprintable))
RE_PUNCT = '[{}]'.format(re.escape(string.punctuation))
RE_UPPER_CLASS = re.compile(r'[A-Z]')
RE_LOWER_CLASS = re.compile(r'[a-z]')
RE_DIGIT_CLASS = re.compile(r'[0-9]')
# \w = r'[a-zA-Z0-9_]'
RE_WORD_CLASS = r'[a-zA-Z0-9_]'

# numerals only allowed at the end of a word, but include it in the word
# hyphens and underscores only allowed at the end of letters before any numerals
# start with an optional dot, then have to have at least 1 letter
# opitonal numerals at the end of word segments, underscores and hyphens between word segments

RE_WORD = r'^([a-zA-Z][-_a-zA-Z]*[\w0-9])[\W]*$'
CRE_WORD = re.compile(RE_WORD)
# RE_WORD_UNGROUPED = r'[a-zA-Z][-_a-zA-Z]*[\w0-9]'

RE_WORD_BASIC = r'[.]?[a-zA-Z]+[0-9]*'
RE_WORD_BASIC_B = wrap(RE_WORD_BASIC)
RE_WORD_LIBERAL = r'[-.a-zA-Z0-9_]+'
RE_WORD_LIBERAL_B = wrap(RE_WORD_LIBERAL)
RE_WORD_CAPITALIZED = r'[A-Z][a-z]+[0-9]{0,3}'
RE_WORD_CAPITALIZED_B = r'\b(' + RE_WORD_CAPITALIZED + r')\b'
RE_WORD_ACRONYM = r"[A-Z0-9][A-Z0-9]{1,6}[0-9]{0,2}"
RE_WORD_ACRONYM_B = r'\b(' + RE_WORD_ACRONYM + r')\b'
RE_WORD_LOWERCASE = r'[a-z]+[0-9]{0,3}'
RE_WORD_LOWERCASE_B = r'\b(' + RE_WORD_LOWERCASE + r')\b'
RE_CAMEL_BASIC = '(' + RE_WORD_CAPITALIZED + r'){2,6}'
RE_CAMEL_BASIC_B = r'\b(' + RE_CAMEL_BASIC + r')\b'
RE_CAMEL_BASIC_LONG = '(' + RE_WORD_CAPITALIZED + r'){7,256}'
RE_CAMEL_BASIC_LONG_B = r'\b(' + RE_CAMEL_BASIC + r')\b'
RE_CAMEL_NORMAL = '(' + RE_CAMEL_BASIC + ')|([a-z]+(' + RE_WORD_CAPITALIZED + r'){1,5})'
RE_CAMEL_NORMAL_B = r'\b(' + RE_CAMEL_NORMAL + r')\b'
RE_CAMEL_LIBERAL = (r'\b(' +
                    '(' + RE_CAMEL_NORMAL + ')|' +
                    '(' + RE_WORD_ACRONYM + '(' + RE_WORD_CAPITALIZED + r'){1,5}' + ')|' +
                    '(' + '[a-z]{0,24}(' + RE_WORD_CAPITALIZED + r'){1,5}' + RE_WORD_ACRONYM + ')' +
                    r')\b')
RE_CAMEL_LIBERAL_B = r'\b(' + RE_CAMEL_LIBERAL + r')\b'
CRE_CAMEL_LIBERAL_B = re.compile(RE_CAMEL_LIBERAL_B)
RE_CAMEL = RE_CAMEL_LIBERAL
RE_CAMEL_B = RE_CAMEL_LIBERAL_B

CHARS_ALGEBRA = r"-+*/^!=().a-zA-Z0-9_'"
RE_WORD_ALGEBRA = '[' + CHARS_ALGEBRA + ']+'

QUOTE_CHARS = "\"'`’"
RE_WORD_BASIC_QUOTED = '|'.join(c + RE_WORD_BASIC + c for c in QUOTE_CHARS)
RE_WORD_LIBERAL_QUOTED = '|'.join(c + RE_WORD_LIBERAL + c for c in QUOTE_CHARS)
RE_WORD_ALGEBRA_QUOTED = '|'.join(c + RE_WORD_ALGEBRA + c for c in QUOTE_CHARS)
RE_PHRASE_BASIC_QUOTED = '|'.join(c + '((' + RE_WORD_BASIC + r')|\W)+' + r'\W?' + c for c in QUOTE_CHARS)
RE_PHRASE_LIBERAL_QUOTED = '|'.join(c + '((' + RE_WORD_LIBERAL + r')|\W)+' + c for c in QUOTE_CHARS)
RE_PHRASE_ALGEBRA_QUOTED = '|'.join(c + '((' + RE_WORD_ALGEBRA + r')|\W)+' + c for c in QUOTE_CHARS)

# 2 to 3 "words" joined by internal underscores is just an underscored word
RE_WORD_UNDERSCORED = '|'.join('[_]+'.join([RE_WORD_BASIC] * i) for i in range(2, 4))
# 4 to 64 "words" joined by internal underscores is a "PHRASE", like the title of a book or file
RE_PHRASE_UNDERSCORED = '|'.join('[_]+'.join([RE_WORD_BASIC] * i) for i in range(4, 65))
# 2 to 3 "words" joined by internal hyphens is just a hyphenated (compound) word
RE_WORD_HYPHENATED = '|'.join('[_]+'.join([RE_WORD_BASIC] * i) for i in range(2, 4))
# 4 to 64 "words" joined by internal hyphens is a "PHRASE"
RE_PHRASE_HYPHENATED = '|'.join('[_]+'.join([RE_WORD_BASIC] * i) for i in range(4, 65))

# based on pci/unused/chapter3/generatefeedvector.py
RE_HTML_TAG = r'[\s]*<[^>]+>[\s]*'
RE_DOUBLEQUOTE = r'["]+'
# \d = [0-9]  # also unicode numerals in all scripts (but only in unicode-supporting flavors unlike Java)
# \w = [a-zA-Z0-9_]

CHARS_LOWER = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
CHARS_UPPER = ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1))
CHARS_DIGIT = ''.join(chr(i) for i in range(ord('0'), ord('9') + 1))
CHARS_ALPHA = CHARS_LOWER + CHARS_UPPER
CHARS_ALPHANUM = CHARS_ALPHA + CHARS_DIGIT
RE_CLASS_ALPHANUM = '[a-zA-Z0-9]'

# Dots and allowed to delimit words, none of the 3 apostrophes nor & symbol do
RE_WORD_DELIM = r"[^-&a-zA-Z0-9_" + APOSTROPHE_CHARS + r"]"
# FIXME: Only single-hyphenated words are accecpted, unaccptable-multi-hyphenated words
RE_HYPHENATED_ALPHA = r"\w+\-\w+"
RE_HYPHENATED_ALPHA_B = r'\b(' + RE_HYPHENATED_ALPHA + r')\b'
RE_HYPHENATED_ALPHANUM = r"[a-zA-Z]\w*\-\w*[a-zA-Z][0-9]*"
RE_HYPHENATED_ALPHANUM_B = r'\b(' + RE_HYPHENATED_ALPHANUM + r')\b'
RE_DOT_PREFIXED_ALPHANUM = '[.]' + RE_WORD_BASIC
RE_DOT_PREFIXED_ALPHANUM_B = r'\b(' + RE_DOT_PREFIXED_ALPHANUM + r')\b'
RE_DOT_PREFIXED_HYPHENATED_ALPHANUM = '[.]' + RE_HYPHENATED_ALPHANUM
RE_DOT_PREFIXED_HYPHENATED_ALPHANUM_B = r'\b(' + RE_DOT_PREFIXED_HYPHENATED_ALPHANUM + r')\b'
# for .Net or .Netable
RE_HYPHENATED_DOTTED_ALPHANUM = r"[a-zA-Z]\w*[-.]\w*[a-zA-Z][0-9]*"
RE_HYPHENATED_DOTTED_ALPHANUM_B = r'\b(' + RE_HYPHENATED_DOTTED_ALPHANUM + r')\b'

# FIXME: Plural words at end single quotes around plural words to be interpretted as possessive
RE_POSESSIVE_ALPHA = r"\w+'[sS]|\w+\-\w+[sS]'|\w+\-\w+"
RE_POSESSIVE_ALPHA_B = r'\b(' + RE_POSESSIVE_ALPHA + r')\b'
RE_HYPHENATED_POSESSIVE_ALPHA = r"\w+\-\w+'[sS]|\w+\-\w+[sS]'|\w+\-\w+"
RE_HYPHENATED_POSESSIVE_ALPHA_B = r'\b(' + RE_HYPHENATED_POSESSIVE_ALPHA + r')\b'

# This will accept a lot of mispelled or nonsense "contractions" and mis some odd, but valid ones listed here:
#    https://en.wikipedia.org/wiki/Wikipedia:List_of_English_contractions
RE_UNHYPHENATED_CONTRACTED_ALPHA = r"['`’]tis|['`’]twas|\w+['`’][a-zA-Z]{1,2}|\w+"
RE_UNHYPHENATED_CONTRACTED_ALPHA_B = r'\b(' + RE_UNHYPHENATED_CONTRACTED_ALPHA + r')\b'
RE_USD_DECIMAL_BMK = r'\$\d+[.]\d+[BMKk]'
RE_USD_DECIMAL_BMK_B = r'\b(' + RE_USD_DECIMAL_BMK + r')\b'
RE_USD_BMK = r'\$[\d]+[BMKk]'
RE_USD_BMK_B = r'\b(' + RE_USD_BMK + r')\b'
RE_USD_CENTS = r'\$\d+[.]\d\d'  # don't allow decidollars or millidollars?
RE_USD_CENTS_B = r'\b(' + RE_USD_CENTS + r')\b'
RE_USD = r'\$[\d]+'
RE_USD_B = r'\b(' + RE_USD + r')\b'
# TODO: add EU and Asian Currencies and decimal formats (swap comma and decimal)
RE_FLOAT = r'[\d]+[.]?\d*'
RE_FLOAT_B = r'\b(' + RE_FLOAT + r')\b'
RE_FLOAT_E = r'[\d]+[.]?\d*[ ]?[eE][ ]?\d+'
RE_FLOAT_E_B = r'\b(' + RE_FLOAT_E + r')\b'
RE_NONSPACE = r'\S+'
RE_NONSPACE_B = r'\b(' + RE_NONSPACE + r')\b'
RE_NONWORD = r'[^\s\w]+'
RE_NONWORD_B = r'\b(' + RE_NONWORD + r')\b'
RE_YEAR = r"\b19\d\d\b|\b20\d\d\b|\b[']?\d\d\b"
RE_YEAR_B = r'\b(' + RE_YEAR + r')\b'
RE_DECADE = r"\b19\d0[']?s\b|\b20\d0[']?s\b|\b[']?\d0[']?s\b"
RE_DECADE_B = r'\b(' + RE_DECADE + r')\b'

RE_ACRONYM = r"[A-Z0-9][A-Z0-9]{1,5}[0-9]{0,2}"
RE_ACRONYM_B = r'\b(' + RE_ACRONYM + r')\b'
# only very narrow, but common examples fit: U.S., U.S.A., A., and B.
RE_DOTTED_ACRONYM_B = r"\b[A-Z][.][A-Z][.][A-Z][.][A-Z][.]\b|\b[A-Z][.][A-Z][.][A-Z][.]\b|\b[A-Z][.][A-Z][.]\b|\b[A-Z][.]\b"
# RE_DOT_NET = r"\b[.]\w[.][A-Z][.][A-Z][.]\b|\b[A-Z][.][A-Z][.][A-Z][.]\b|\b[A-Z][.][A-Z][.]\b|\b[A-Z][.]\b"

# # Wrap token RE w/ parens (in case it contains ORs) and add nonconsuming word break (\b) at the end
# for name in ('WORD_CAPITALIZED', 'WORD_LOWERCASE', 'ACRONYM', 'USD_BMK', 'USD_CENTS', 'USD_DECIMAL_BMK',
#              'POSESSIVE_ALPHA', 'HYPHENATED_POSESSIVE_ALPHA'
#              'FLOAT_E', 'FLOAT_E', 'NONSPACE'):
#     name = 'RE_' + name
#     # this will hose up flake8
#     locals()[name + '_B'] = r'(' + locals()[name] + r')\b'

# RE_CAMEL_CASE = ('(((' + RE_WORD_CAPITALIZED_B + ')|(' + RE_WORD_LOWERCASE + '))' + '(' + RE_ACRONYM + '))|' +
#                  '((' + RE_ACRONYM + '|' + RE_WORD_CAPITALIZED + '|' + RE_WORD_LOWERCASE + ')+(' + RE_WORD_CAPITALIZED + ')+)' + r'\b')
# RE_CAMEL_CASE = CRE_CAMEL_CASE = re.compile(RE_CAMEL_CASE)

# always list RE's from most greedy to least greedy []+, []*, []?, then [], supersets before subsets in char groups []
RE_TOKEN = r'|'.join(['[.]' + RE_HYPHENATED_ALPHANUM, RE_HYPHENATED_ALPHA,
                      RE_HYPHENATED_ALPHANUM,
                      RE_UNHYPHENATED_CONTRACTED_ALPHA_B,
                      RE_USD_DECIMAL_BMK, RE_USD_BMK_B, RE_USD_CENTS, RE_USD,
                      RE_DECADE, RE_YEAR,
                      RE_ACRONYM,
                      RE_FLOAT_E, RE_FLOAT,
                      RE_NONWORD])
RE_TOKEN = r'|'.join([RE_DOUBLEQUOTE,
                      RE_USD_DECIMAL_BMK_B, RE_USD_BMK_B, RE_USD_CENTS_B, RE_USD_B,
                      RE_DECADE_B, RE_YEAR_B,
                      RE_ACRONYM_B,
                      RE_FLOAT_E_B, RE_FLOAT_B,
                     '[.]' + RE_HYPHENATED_ALPHANUM_B,
                      RE_HYPHENATED_POSESSIVE_ALPHA_B,
                      RE_HYPHENATED_DOTTED_ALPHANUM_B,
                      # FIXME: Plural words at end single quotes around plural words to be interpretted as possessive
                      RE_POSESSIVE_ALPHA_B,
                      RE_HYPHENATED_ALPHA_B,
                      RE_HYPHENATED_ALPHANUM_B,
                      RE_UNHYPHENATED_CONTRACTED_ALPHA_B,
                      RE_NONWORD])
LIST_RE_TOKEN_NAMED = [
    'RE_USD_DECIMAL_BMK',
    'RE_USD_BMK',
    'RE_USD_CENTS',
    'RE_USD',
    'RE_DECADE',
    'RE_YEAR',
    'RE_ACRONYM',
    'RE_FLOAT_E',
    'RE_FLOAT',
    'RE_HYPHENATED_ALPHA',
    'RE_UNHYPHENATED_CONTRACTED_ALPHA',
    'RE_NONWORD']
RE_TOKEN_NAMED = r'|'.join(['(?P<{}>{})'.format(rename.lower()[3:], locals()[rename]) for rename in LIST_RE_TOKEN_NAMED])

CRE_WORD_DELIM = re.compile(RE_WORD_DELIM)
CRE_HTML_TAG = re.compile(RE_HTML_TAG)
CRE_TOKEN = re.compile(RE_TOKEN)

RE_BAD_FILENAME = '[{}]'.format(re.escape(string.punctuation.replace('-', '').replace('_', '') + string.unprintable))
CRE_BAD_FILENAME = re.compile(RE_BAD_FILENAME)
CRE_WHITESPACE = re.compile(r'\s')


#####################################################
# IDE and code refactoring regexes
# Tested in Sublime Text 2

# Find redefinitions of the same regex in the same file
RE_REDEF = r'(\n[C]?RE_[A-Z_]+[ ])[\w\W]*\1'
