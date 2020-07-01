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

np.set_printoptions(threshold=np.inf)
# Loading data in from npy files (more efficent that txt or similar, see master for creation)
events_array = np.load("data/events_array.npy")
pmt_array = np.load("data/pmt_array.npy")
pmt_peak_freq = np.load("data/pmt_peak_freq.npy")



#Global Constants
TEL_PIXEL_COUNT = len(pmt_array)



for i in range(TEL_PIXEL_COUNT):
    if i== 128 or i==173 or i==259:
        continue
    else:

        freq_counter, index = np.unique(pmt_array[i], return_counts=True)



        num_events = len(pmt_array[0])                               # Data size
        mean = sum(freq_counter*index)/num_events                    # Mean of pixel value
        sigma = sum(index*(freq_counter-mean)**2)/num_events         # Varianvce of the data

        #print(i)



        def gaus(x,a,x0,sigma):
            return a*np.exp(-(x-x0)**2/(2*sigma**2))

        popt,pcov = curve_fit(gaus, freq_counter, index, p0=[1,mean,sigma], maxfev=1000000)

        plt.plot(freq_counter, index, label=')Data')
        plt.xlim(0, 100)


        #print("The average peak value was: {0:.2f}".format(np.average(pmt_peak_freq)))
        #print("The mean of the mean of gaussian fit is: {0:.2f}".format(mean))
        #print("The standard deveiation is: {0:0.2f}".format(sigma**.5))

        plt.text(35,110, 'Mean = {0:.2f}\nStandard Deviation = {1:.2f}\nAverage Peak = {2:.2f}'.format(mean, sigma**.5, np.average(pmt_peak_freq)))
        plt.plot(freq_counter,gaus(freq_counter,*popt),'ro:',label='Gauss Fit')
        plt.legend()
        plt.title('Frequency plot for PMPIX_1')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.savefig('output/freq_pmpix/pdf/freq_pmpix_{}.pdf'.format(i+1))
        plt.cla()





