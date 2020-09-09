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
pmt_mean_values = np.load("data/pmt_mean_values.npy")
pmt_variance_values = np.load("data/pmt_variance_values.npy")
x_coords = np.load("data/x_coords.npy")
y_coords = np.load("data/y_coords.npy")

TEL_PIXEL_COUNT = len(pmt_array)

pmt_mean_values = pmt_mean_values.astype('float64')
pmt_variance_values = pmt_variance_values.astype('float64')




mean_of_mean = np.nanmean(pmt_mean_values)
mean_of_variances = np.nanmean(pmt_variance_values)
variance_of_mean_of_means = np.nanvar(pmt_mean_values)




color_map_min = int(mean_of_mean + (3 * (mean_of_variances ** 0.5)))
color_map_max = int(mean_of_mean + (25 * (mean_of_variances ** 0.5)))


cherenkov_array =( np.copy(events_array) - color_map_min ).clip(0)

np.save("data/cherenkov_array.npy", cherenkov_array)
exit()


#gradiant = np.linspace((mean_of_mean + (3 * (mean_of_variances ** 0.5))), mean_of_mean + (8 * (mean_of_variances ** 0.5)), num=256)





def TelescopePlot(current_event, index):
    # Generates the Plot of the telescope for a given event.


    event_colourmap = np.clip(current_event, 0, color_map_max)
    #pix_color = []
    for i in range(TEL_PIXEL_COUNT):
        # Gets the telescope Details and coordinates for pixels, and plots them according to PixelDetection




        #pix_color.append(PixelDetection(current_event[i]))
        #print(pix_color[i])
        #plt.plot(x_coords[i], y_coords[i], 'h', color=pix_color, markersize=8, linestyle="None")
        if current_event[i] > 0:
            plt.text(x_coords[i]-5, y_coords[i], current_event[i], fontsize=2)   # Adds pixel number to plot


    plt.scatter(x_coords, y_coords, s=32, c=event_colourmap, cmap='magma', marker='h', vmax=color_map_max)
    # Finishing the Plot for the telescope
    ax.set_title("PMPIX of event {}".format(index + 1))
    #cbar = plt.colorbar()
    ax.set_xlabel("X Coords of Telescope")
    ax.set_ylabel("Y Coords of Telescope")
    if index==0:
        plt.colorbar()
    plt.draw()
    fig.savefig('output/telescope_image/output_plot_event_{0}.pdf'.format(index + 1), bbox_inches='tight')

    plt.cla()




fig, ax = plt.subplots()
#fig.colorbar(ax, 'magma')
#image, = ax.plot(x_coords, y_coords, markersize=8, linestyle="None")
#fig.x_label("x")
#ax.set_ylabel("y")



for count, element in enumerate(cherenkov_array):
    #print(count)
    TelescopePlot(element, count)


    #exit()
    #if count == 10:
        #exit()
