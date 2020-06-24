#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:56:00 2020

@author: cormac
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab as plb
from scipy.optimize import curve_fit
import collections as col
# Loading data in from npy files (more efficent that txt or similar, see master for creation)
events_array = np.load("data/events_array.npy")
pmt_array = np.load("data/pmt_array.npy")
pmt_peak_freq = np.load("data/pmt_peak_freq.npy")



freq_counter, index = np.unique(pmt_array[0], return_counts=True)



#x = np.asarray(range(10))
#y = np.asarray([0,1,2,3,4,5,4,3,2,1])

n = len(pmt_array[0])                          #the number of data
mean = sum(freq_counter*index)/n                   #note this correction
sigma = sum(index*(freq_counter-mean)**2)/n        #note this correction

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt,pcov = curve_fit(gaus, freq_counter, index, p0=[1,mean,sigma])


plt.plot(freq_counter, index, label='Data')
plt.xlim(0, 100)



print("The average peak value was: {0:.2f}".format(np.average(pmt_peak_freq)))
print("The mean of the mean of gaussian fit is: {0:.2f}".format(mean))
print("The standard deveiation is: {0:0.2f}".format(sigma**.5))

plt.text(35,110, 'Mean = {0:.2f}\nStandard Deviation = {1:.2f}\nAverage Peak = {2:.2f}'.format(mean, sigma**.5, np.average(pmt_peak_freq)))
plt.plot(freq_counter,gaus(freq_counter,*popt),'ro:',label='Gauss Fit')
plt.legend()
plt.title('Frequency plot for PMPIX_1')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.savefig('output/freq_pmpix_1.png')





