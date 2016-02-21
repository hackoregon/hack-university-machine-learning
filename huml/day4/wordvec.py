import re

import pandas as pd
np = pd.np

from regex import CRE_TOKEN, CRE_HTML_TAG, RE_NONWORD

INF = pd.np.inf
NAN = pd.np.nan
NAT = pd.NaT


def safe_mod(a, b, inf_factor=1.):
    """Calculate remainder for integer division (mod) without ZeroDivisionError exceptions

    Arguments:
      a (float or int): numerator of division
      b (float or int): divisor
      inf_factor (float or int): factor to multiply numerator (`a`) by to compute return value for ZeroDivisionError

    Return:
      int: remainder after dividing a by b
    """
    try:
        return a % b
    except ZeroDivisionError:
        return inf_factor * a
    except TypeError:
        # figure out which obj is not an int and return it
        try:
            1 % b
        except TypeError:
            return b
        return a
    return a % b


def safe_div(a, b, inf=INF):
    """Safely divide by zero and inf and nan and produce floating point result

    Numerical results are equivalent to `from future import division`

    Args:
      a (float or int): numerator
      b (float or int): denominator
      inf (float or object): value to return in place of division by zero errors
      none (float or object): value to return in place of TypeErrors (division by None)

    Returns:
      dividend:
        b if b is None or NaN
        a if a is None or NaN
        inf (specified by caller, default is np.inf) if b is 0
        pd.NaT if b or a is pd.NaT

    >>> safe_div(84, 2)
    42.0
    >>> safe_div(-85, 2)
    -42.5
    >>> safe_div(42, 0)
    inf
    >>> safe_div(-42, 0)
    inf
    >>> safe_div(1, 0.)
    inf
    >>> safe_div(1, 0., inf="custom OutOfBounds str")
    'custom OutOfBounds str'
    >>> safe_div(np.inf, np.inf)
    nan
    >>> safe_div(1e200, np.inf)
    0.0
    >>> safe_div(np.inf, np.nan)
    nan
    >>> safe_div(np.nan, 0)
    inf
    >>> repr(safe_div(99.99, None))
    'None'
    >>> safe_div(42, object())
    <object object at 0x...>
    """
    try:
        return 1. * a / b
    except ZeroDivisionError:
        return inf
    except TypeError:
        try:
            1. / b
        except TypeError:
            return b
        return a
    return 1. * a / b


def norm(d, **kwargs):
    """Norm of scipy sparse matrix (1-D), python dict, or pd.Series

    >>> d = pd.Series([2,0,1,1,1,1,1], index=[1, 3, 7, 42, 84, 126, 168])
    >>> norm(d)
    3.0
    """
    try:
        return np.linalg.norm(d.values(), **kwargs)
    except (TypeError, AttributeError):
        return np.linalg.norm(d, **kwargs)


def dot(d1, d2, scalar=None):
    """Dot (inner) product of two dicts or sparse matrices or pd.Series

    >>> d = pd.Series([1,0,1,1], index=[1, 3, 7, 42])
    >>> dot(d, d)
    3
    >>> d = dict(zip(d.index, d))
    >>> dot(d, d)
    3
    >>> import scipy.sparse
    >>> d = [d.get(k, 0) for k in range(max(d.keys()) + 1)]
    >>> d = scipy.sparse.csr_matrix(d)
    >>> dot(d, d)
    3
    """
    if hasattr(d1, 'keys') and callable(d1.keys):
        return np.sum(d1[k] * d2[k] for k in (set(d1.keys()) & set(d2.keys())))

    # d1 and d2 must be scipy sparse matrices or pd.Series or np.arrays
    try:
        return np.dot(d1, d2)
    except:
        if len(getattr(d1, 'shape', [])) == 2:
            if d1.shape[0] <= d1.shape[-1]:
                ans = d1 * d1.T
            else:
                ans = d1.T * d1
        else:
            ans = np.array(d1) * np.array(d2)
    if hasattr(ans, 'todense') and (scalar or (scalar is None and ans.shape[0] == 1)):
        return ans.todense()[0, 0]
    return ans


def cosine_similarity(d1, d2, **np_norm_kwargs):
    r"""Compute the inverse cosine similarity between two sparse vectors (dicts)

    >>> cosine_similarity({'a': 1, 'b': 2, 'c': -1}, {'a': 1, 'c': 1, 'd': -1})
    0.0
    """
    n1 = norm(d1, **np_norm_kwargs) or 1.
    n1 = n1 if n1 is not np.nan else 1.
    n2 = norm(d2, **np_norm_kwargs) or 1.
    n2 = n2 if n2 is not np.nan else 1.

    return dot(d1, d2) * safe_div(1, n1 * n2)


def cosine_distance(d1, d2, **np_norm_kwargs):
    r"""Compute the inverse cosine similarity between two sparse vectors (dicts)

    >>> cosine_distance({'a': 1, 'b': 2, 'c': -1}, {'a': 1, 'c': 1, 'd': -1})
    inf
    """
    return safe_div(1, cosine_similarity(d1, d2))


def strip_html(html):
    r"""Extract text from HTML string, stripping tags & superfluous whitespace

    HTML tags are replaced with newlines ('\n') and repeated newlines are consolidated.

    >>> strip_html(u"Even<h1><bold id=bolded>invalid html</bold></sm>is stripped.")
    u'Even\ninvalid html\nis stripped.'
    """
    return '\n'.join(line.strip() for line in CRE_HTML_TAG.sub('\n', html).split('\n') if line.strip())


def generate_tokens(doc, regex=CRE_TOKEN, strip=True, nonwords=False):
    r"""Return a sequence of words or tokens, using a re.match iteratively through the str

    >>> doc = "John D. Rock\n\nObjective: \n\tSeeking a position as Software --Architect-- / _Project Lead_ that can utilize my expertise and"
    >>> doc += " experiences in business application development and proven records in delivering 90's software. \n\nSummary: \n\tSoftware Architect"
    >>> doc += " who has gone through several full product-delivery life cycles from requirements gathering to deployment / production, and"
    >>> doc += " skilled in all areas of software development from client-side JavaScript to database modeling. With strong experiences in:"
    >>> doc += " \n\tRequirements gathering and analysis."
    >>> len(list(generate_tokens(doc, strip=False, nonwords=True)))
    82
    >>> seq = list(generate_tokens(doc, strip=False, nonwords=False))
    >>> len(seq)
    70
    >>> '.' in seq or ':' in seq
    False
    >>> s = set(generate_tokens(doc, strip=False, nonwords=True))
    >>> all(t in s for t in ('D', '.', ':', '_Project', 'Lead_', "90's", "Architect", "product-delivery"))
    True
    """
    if isinstance(regex, basestring):
        regex = re.compile(regex)
    for w in regex.finditer(doc):
        if w:
            w = w.group()
            if strip:
                w = w.strip(r'-_*`()}{' + r"'")
            if w and (nonwords or not re.match(r'^' + RE_NONWORD + '$', w)):
                yield w
