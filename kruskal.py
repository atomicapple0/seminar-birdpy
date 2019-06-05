def kruskal(*args, **kwargs):
    args = list(map(np.asarray, args))
    num_groups = len(args)
    if num_groups < 2:
        raise ValueError("Need at least two groups in stats.kruskal()")

    for arg in args:
        if arg.size == 0:
            return KruskalResult(np.nan, np.nan)
    n = np.asarray(list(map(len, args)))

    if 'nan_policy' in kwargs.keys():
        if kwargs['nan_policy'] not in ('propagate', 'raise', 'omit'):
            raise ValueError("nan_policy must be 'propagate', "
                             "'raise' or'omit'")
        else:
            nan_policy = kwargs['nan_policy']
    else:
        nan_policy = 'propagate'

    contains_nan = False
    for arg in args:
        cn = _contains_nan(arg, nan_policy)
        if cn[0]:
            contains_nan = True
            break

    if contains_nan and nan_policy == 'omit':
        for a in args:
            a = ma.masked_invalid(a)
        return mstats_basic.kruskal(*args)

    if contains_nan and nan_policy == 'propagate':
        return KruskalResult(np.nan, np.nan)

    alldata = np.concatenate(args)
    ranked = rankdata(alldata)
    ties = tiecorrect(ranked)
    if ties == 0:
        raise ValueError('All numbers are identical in kruskal')

    # Compute sum^2/n for each group and sum
    j = np.insert(np.cumsum(n), 0, 0)
    ssbn = 0
    for i in range(num_groups):
        ssbn += _square_of_sums(ranked[j[i]:j[i+1]]) / float(n[i])

    totaln = np.sum(n)
    h = 12.0 / (totaln * (totaln + 1)) * ssbn - 3 * (totaln + 1)
    df = num_groups - 1
    h /= ties

    return KruskalResult(h, distributions.chi2.sf(h, df))

def rankdata(a, method='average'):
    """
    rankdata(a, method='average')
    Assign ranks to data, dealing with ties appropriately.
    Ranks begin at 1.  The `method` argument controls how ranks are assigned
    to equal values.  See [1]_ for further discussion of ranking methods.
    Parameters
    ----------
    a : array_like
        The array of values to be ranked.  The array is first flattened.
    method : str, optional
        The method used to assign ranks to tied elements.
        The options are 'average', 'min', 'max', 'dense' and 'ordinal'.
        'average':
            The average of the ranks that would have been assigned to
            all the tied values is assigned to each value.
        'min':
            The minimum of the ranks that would have been assigned to all
            the tied values is assigned to each value.  (This is also
            referred to as "competition" ranking.)
        'max':
            The maximum of the ranks that would have been assigned to all
            the tied values is assigned to each value.
        'dense':
            Like 'min', but the rank of the next highest element is assigned
            the rank immediately after those assigned to the tied elements.
        'ordinal':
            All values are given a distinct rank, corresponding to the order
            that the values occur in `a`.
        The default is 'average'.
    Returns
    -------
    ranks : ndarray
         An array of length equal to the size of `a`, containing rank
         scores.
    References
    ----------
    .. [1] "Ranking", http://en.wikipedia.org/wiki/Ranking
    Examples
    --------
    >>> from scipy.stats import rankdata
    >>> rankdata([0, 2, 3, 2])
    array([ 1. ,  2.5,  4. ,  2.5])
    >>> rankdata([0, 2, 3, 2], method='min')
    array([ 1,  2,  4,  2])
    >>> rankdata([0, 2, 3, 2], method='max')
    array([ 1,  3,  4,  3])
    >>> rankdata([0, 2, 3, 2], method='dense')
    array([ 1,  2,  3,  2])
    >>> rankdata([0, 2, 3, 2], method='ordinal')
    array([ 1,  2,  4,  3])
    """
    if method not in ('average', 'min', 'max', 'dense', 'ordinal'):
        raise ValueError('unknown method "{0}"'.format(method))

    arr = np.ravel(np.asarray(a))
    algo = 'mergesort' if method == 'ordinal' else 'quicksort'
    sorter = np.argsort(arr, kind=algo)

    inv = np.empty(sorter.size, dtype=np.intp)
    inv[sorter] = np.arange(sorter.size, dtype=np.intp)

    if method == 'ordinal':
        return inv + 1

    arr = arr[sorter]
    obs = np.r_[True, arr[1:] != arr[:-1]]
    dense = obs.cumsum()[inv]

    if method == 'dense':
        return dense

    # cumulative counts of each unique value
    count = np.r_[np.nonzero(obs)[0], len(obs)]

    if method == 'max':
        return count[dense]

    if method == 'min':
        return count[dense - 1] + 1

    # average method
    return .5 * (count[dense] + count[dense - 1] + 1)
    
def tiecorrect(rankvals):
    """
    Tie correction factor for ties in the Mann-Whitney U and
    Kruskal-Wallis H tests.
    Parameters
    ----------
    rankvals : array_like
        A 1-D sequence of ranks.  Typically this will be the array
        returned by `stats.rankdata`.
    Returns
    -------
    factor : float
        Correction factor for U or H.
    See Also
    --------
    rankdata : Assign ranks to the data
    mannwhitneyu : Mann-Whitney rank test
    kruskal : Kruskal-Wallis H test
    References
    ----------
    .. [1] Siegel, S. (1956) Nonparametric Statistics for the Behavioral
           Sciences.  New York: McGraw-Hill.
    Examples
    --------
    >>> from scipy.stats import tiecorrect, rankdata
    >>> tiecorrect([1, 2.5, 2.5, 4])
    0.9
    >>> ranks = rankdata([1, 3, 2, 4, 5, 7, 2, 8, 4])
    >>> ranks
    array([ 1. ,  4. ,  2.5,  5.5,  7. ,  8. ,  2.5,  9. ,  5.5])
    >>> tiecorrect(ranks)
    0.9833333333333333
    """
    arr = np.sort(rankvals)
    idx = np.nonzero(np.r_[True, arr[1:] != arr[:-1], True])[0]
    cnt = np.diff(idx).astype(np.float64)

    size = np.float64(arr.size)
    return 1.0 if size < 2 else 1.0 - (cnt**3 - cnt).sum() / (size**3 - size)