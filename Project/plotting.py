#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:56:00 2020

@author: cormac
"""

import numpy as np
import matplotlib.pyplot as plt

events_array = np.load("data/events_array.npy")
pmt_array = np.load("data/pmt_array.npy")
pmt_peak_freq = np.load("data/pmt_peak_freq.npy")



def PulseHeightSpectrum(pmt):
    for count, element in enumerate(pmt):
        plt.hist(element, bins=np.arange(30, 100))
        pmt_peak_freq[count] = np.bincount(element).argmax()


        plt.savefig('output/pulse_spectrum/output_pulse_spectrumt_{0}.png'.format(count + 1), bbox_inches='tight')
        plt.cla()
#PulseHeightSpectrum(pmt_array)



def PixelDetection(pix_num):
    if pix_num >= 20:
        return 'blue'
    else:
        return 'gray'







def TelescopePlot(current_event, index):
    # Generates the Plot of the telescope for a given event.



    pix_color = []
    for i in range(TEL_PIXEL_COUNT):
        # Gets the telescope Details and coordinates for pixels, and plots them according to PixelDetection

        pix_color.append(PixelDetection(current_event[i]))
        #print(pix_color[i])
        #plt.plot(x_coords[i], y_coords[i], 'h', color=pix_color, markersize=8, linestyle="None")
        #plt.text(x_array[i], y_array[i], i)   # Adds pixel number to plot


    plt.scatter(x_coords, y_coords, s=64, c=pix_color, marker='h')
    # Finishing the Plot for the telescope
    ax.set_title("PMPIX of event {}".format(index + 1))
    plt.draw()
    fig.savefig('output/telescope_image/output_plot_event_{0}.pdf'.format(index + 1), bbox_inches='tight')


    plt.cla()



fig, ax = plt.subplots()
#image, = ax.plot(x_coords, y_coords, markersize=8, linestyle="None")
ax.set_xlabel("x")
ax.set_ylabel("y")
"""
pix_color = []
for i in range(TEL_PIXEL_COUNT):
    pix_color.append(PixelDetection(events_array[i][i]))

plt.scatter(x_coords, y_coords, s=8, c=pix_color, marker='h')
"""

for count, element in enumerate(events_array):
    print(count)
    #TelescopePlot(element, count)
    exit()
