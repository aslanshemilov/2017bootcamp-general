# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:12:35 2017

@author: sheila
"""

import multiprocessing
import time

def funSquare(num):
    return num ** 2

if __name__ == '__main__':
    nums=range(10000000)     
    poola = multiprocessing.Pool(1) #initializes N workers, where N = # of CPU cores
    poolb = multiprocessing.Pool(10) #initializes N workers, where N = # of CPU cores
    tic1 = time.clock()
    results1 = poola.map(funSquare, nums)
    toc1 = time.clock()
    tic2 = time.clock()
    results12 = poolb.map(funSquare, nums)
    toc2 = time.clock()
    tic3 = time.clock()
    resultsseq = map(funSquare, nums)
    toc3 = time.clock()
    print('Parallel processing time (1, 10 proc): %r %r\nSerial processing time: %r'
          % (toc1 - tic1, toc2 - tic2, toc3 - tic3))