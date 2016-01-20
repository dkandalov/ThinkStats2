"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import math

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.
    hist: Hist object
    returns: value from Hist
    """
    freq, value = max([(freq, value) for value, freq in hist.Items()])
    return value


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.
    hist: Hist object
    returns: iterator of value-freq pairs
    """
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)


def cohen_effect_size(group1, group2):
    diff = group1.mean() - group2.mean()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * group1.var() + n2 * group2.var()) / (n1 + n2)
    return diff / math.sqrt(pooled_var)


def WeightDifference(firsts, others):
    mean_diff = firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()
    c_diff = cohen_effect_size(firsts.totalwgt_lb, others.totalwgt_lb)
    return mean_diff, c_diff


def main(script):
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)

    print("Mean diff and Cohen d: {0}".format(WeightDifference(firsts, others)))


if __name__ == '__main__':
    main(*sys.argv)
