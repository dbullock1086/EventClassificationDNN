#!/usr/bin/env python

import numpy as np

def CSVWriter (filename, X, Y, R, arrType):
    names = X.dtype.names
    colnames = []

    for n in names: colnames.append(n)
    for i in xrange(0, Y.shape[1]): colnames.append('true_' + str(i))
    for i in xrange(0, R.shape[1]): colnames.append('predict_' + str(i))

    f = open(filename, 'w')
    f.write(','.join(colnames) + '\n')

    X0 = X.view(arrType).reshape(X.shape + (-1,))
    out = np.concatenate((X0,Y,R), axis=1)

    np.savetxt(f, out, delimiter=',')
    pass
