"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import sys

import thinkstats2
import thinkplot


def ReadFile(filename):
    """Reads a list of numbers from a file.

    filename: string

    returns: list of float
    """
    fp = open(filename)
    data = []
    for line in fp:
        x = float(line.strip())
        data.append(x)
    return data


# mystery0 - linear
# mystery1 - normal
# mystery2 - exponential
# mystery3 - normal
# mystery4 - (!) expo/weibull?
# mystery5 - pareto
# mystery6 - (!) normal/weibull?
# mystery7 - (!) exponential

# mystery0.dat uniform_sample
# mystery1.dat triangular_sample
# mystery2.dat expo_sample
# mystery3.dat gauss_sample
# mystery4.dat lognorm_sample
# mystery5.dat pareto_sample
# mystery6.dat weibull_sample
# mystery7.dat gumbel_sample
def main(script, filename='mystery7.dat'):
    data = ReadFile(filename)
    cdf = thinkstats2.Cdf(data)

    thinkplot.PrePlot(rows=2, cols=3)
    thinkplot.SubPlot(1)
    thinkplot.Cdf(cdf)
    thinkplot.Config(title='linear')

    thinkplot.SubPlot(2)
    scale = thinkplot.Cdf(cdf, xscale='log')
    thinkplot.Config(title='logx', **scale)

    thinkplot.SubPlot(3)
    scale = thinkplot.Cdf(cdf, transform='exponential')
    thinkplot.Config(title='expo', **scale)

    thinkplot.SubPlot(4)
    xs, ys = thinkstats2.NormalProbability(data)
    thinkplot.Plot(xs, ys)
    thinkplot.Config(title='normal')

    thinkplot.SubPlot(5)
    scale = thinkplot.Cdf(cdf, transform='pareto')
    thinkplot.Config(title='pareto', **scale)

    thinkplot.SubPlot(6)
    scale = thinkplot.Cdf(cdf, transform='weibull')
    thinkplot.Config(title='weibull', **scale)

    thinkplot.Show(legend=False)


if __name__ == '__main__':
    main(*sys.argv)
