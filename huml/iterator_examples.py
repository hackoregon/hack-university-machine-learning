"""The only 4 ways to create an iterable.

Based on http://stackoverflow.com/a/7542261/623735
"""


def generate(it):
    """Implement a generator: iterate through the sequence and yield each element"""
    for char in it:
        yield char.upper()


def generator_expression(it):
    return (char.upper() for char in it)


class Iterator():
    """Comply with iterator interface (next and __iter__)"""
    def __init__(self, it):
        self.it = it
        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        """For python 2"""
        try:
            result = self.it[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def __next__(self):
        """For python 3"""
        return self.next


class GetItem():
    """Implement a __getitem__ method"""
    def __init__(self, it):
        self.it = it

    def __getitem__(self, index):
        return self.it[index]


## BROKEN
#from itertools import izip


def gen_ngrams(token_seq, n=1, join=' '):
    """Return a list of n-tuples, one for each possible sequence of n items in the token_list

    Arguments:
      join (bool or str): if str, then join ngrom tuples on it before returning
         True is equivalent to join=' '
         default = True

    See: http://stackoverflow.com/a/30609050/623735

    >>> list(gen_ngrams('goodbye cruel world'.split(), join=False))
    [('goodbye',), ('cruel',), ('world',)]
    >>> list(gen_ngrams('goodbye cruel world'.split(), 2, join=False))
    [('goodbye', 'cruel'), ('cruel', 'world')]
    >>> list(gen_ngrams('goodbye cruel world'.split(), 2, join='*'))
    ['goodbye*cruel', 'cruel*world']
    """
    join = ' ' if join is True else join
    print('called with token_seq={}, n={}'.format(token_seq, n))
    if isinstance(join, basestring):
        for k, ngram in enumerate(join.join(ng) for ng in gen_ngrams(token_seq, n=n, join=False)):
            print('join #{}, ngram={}'.format(k, ngram))
            yield ngram
    else:
        for j, ngram in enumerate(zip(*[[tok for j, tok in enumerate(token_seq) if j >= i] for i in range(n)])):
            print('ngram #{}, ngram={}'.format(j, ngram))
            yield ngram
        # for ngram in izip(*((tok for j, tok in enumerate(token_seq) if j >= i) for i in xrange(n))):
        #     yield ngram
