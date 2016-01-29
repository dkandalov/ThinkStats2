import math

import first
import nsfg
import thinkstats2
import thinkplot
from thinkstats2 import Pmf


def PmfMean(pmf):
    mean = 0
    for x, p in pmf.Items():
        mean += p * x
    return mean


def PmfVar(pmf):
    mean = PmfMean(pmf)
    var = 0
    for x, p in pmf.Items():
        var += p * ((x - mean) ** 2)
    return var


def FirstVsOtherPregLength_ForTheSameWoman(live):
    live = live[live.prglngth >= 37]
    live_by_caseid = nsfg.MakePregMap(live)

    diffs = []
    for caseid, indices in live_by_caseid.items():
        preg_lengths = live.loc[indices].prglngth.values
        if (len(preg_lengths) >= 2):
            first = preg_lengths[0]
            rest = preg_lengths[1:]
            diffs.extend([first - it for it in rest])

    mean = thinkstats2.Mean(diffs)
    print("FirstVsOtherPregLength_ForTheSameWoman mean: ", mean)

    pmf = thinkstats2.Pmf(diffs)
    thinkplot.Hist(pmf)
    thinkplot.Show(xlabel='Difference in weeks', ylabel='PMF')


if __name__ == '__main__':
    live, firsts, others = first.MakeFrames()
    pmf = Pmf(firsts.totalwgt_lb)
    assert PmfMean(pmf) == pmf.Mean()
    assert PmfVar(pmf) == pmf.Var()

    FirstVsOtherPregLength_ForTheSameWoman(live)

    print("Done")