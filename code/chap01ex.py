"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemResp(dict_file='2002FemResp.dct',
                data_file='2002FemResp.dat.gz',
                row_count=None):
    dct = thinkstats2.ReadStataDct(dict_file)
    df = dct.ReadFixedWidth(data_file, compression='gzip', nrows=row_count)
    return df


def main(script):
    """Tests the functions in this module.
    script: string script name
    """
    print("Loading data...")
    resp_df = ReadFemResp(row_count=100)
    print("Data shape: {0}".format(resp_df.shape))

    # assert len(resp_df) == 11027
    assert resp_df.caseid[0] == 2298, resp_df.caseid[0]

    had_mismatches = False
    preg_indices_by_caseid = nsfg.MakePregMap(nsfg.ReadFemPreg())
    for index, row in resp_df.iterrows():
        if len(preg_indices_by_caseid[row.caseid]) != row.pregnum:
            print("Mismatching pregnum for {0}".format(row.caseid))
            had_mismatches = True

    if not had_mismatches:
        print('All tests passed for: {0}.'.format(script))


if __name__ == '__main__':
    main(*sys.argv)
