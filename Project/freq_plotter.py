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








pmt_mean_values = np.zeros(TEL_PIXEL_COUNT)
pmt_variance_values = np.zeros(TEL_PIXEL_COUNT)





def Frequency_Count(pixel_array, use_full_set=True, save_format='pdf'):
    for i in range(pixel_array):

        freq_counter, index = np.unique(pmt_array[i], return_counts=True)
        if not use_full_set:
            pmt_temp = pmt_array[i][ pmt_array[i] <= 60 ]
            freq_counter, index = np.unique(pmt_temp, return_counts=True)
            save_name = 'freq_background_pmpix_'
            save_location = 'output/freq_pmpix/background_set/'
        else:
            save_location = 'output/freq_pmpix/full_set/'
            save_name = 'freq_full_pmpix_'


        # Checks for a zeroed pmt_array; Which causes freq_counter to be 0 2500 times. (Also catches if is always 1 or ..)
        if len(freq_counter) == 1:
            continue




        num_events = len(pmt_array[0])                                                              # Data size
        pmt_mean_values[i] = sum(freq_counter*index)/num_events                                     # Mean of pixel value
        pmt_variance_values[i] = sum(index*(freq_counter-pmt_mean_values[i])**2)/num_events            # Varianvce of the data



        def gaus(x,a,x0,sigma):
            return a*np.exp(-(x-x0)**2/(2*sigma**2))

        popt,pcov = curve_fit(gaus, freq_counter, index, p0=[1,pmt_mean_values[i], pmt_variance_values[i]], maxfev=1000000)
        continue
        plt.plot(freq_counter, index, label=')Data')
        plt.xlim(0, 100)



        plt.text(35,110, 'Mean = {0:.2f}\nStandard Deviation = {1:.2f}\nAverage Peak = {2:.2f}'.format(pmt_mean_values[i], pmt_variance_values[i]**.5, np.average(pmt_peak_freq)))
        plt.plot(freq_counter,gaus(freq_counter,*popt),'ro:',label='Gauss Fit')
        plt.legend()
        plt.title('Frequency plot for PMPIX_1')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.savefig('{0}{3}/{1}{2}.{3}'.format(save_location, save_name, i+1, save_format))
        plt.cla()





Frequency_Count(TEL_PIXEL_COUNT, use_full_set=False, save_format='pdf')
#Frequency_Count(TEL_PIXEL_COUNT, use_full_set=False, save_format='png')
#Frequency_Count(TEL_PIXEL_COUNT, use_full_set=True, save_format='pdf')
#Frequency_Count(TEL_PIXEL_COUNT, use_full_set=True, save_format='png')


print(pmt_mean_values)
print(pmt_variance_values)
np.save('data/pmt_mean_values.npy', pmt_mean_values)
np.save('data/pmt_variance_values.npy', pmt_variance_values)
