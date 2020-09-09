#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 9 11:35:15 2020

@author: cormac
"""

import numpy as np
import matplotlib.pyplot as plt


# Array importing
events_array = np.load("data/events_array.npy")
cherenkov_array = np.load("data/cherenkov_array.npy")
#pmt_array = np.load("data/pmt_array.npy")
#pmt_peak_freq = np.load("data/pmt_peak_freq.npy")
#pmt_mean_values = np.load("data/pmt_mean_values.npy")
#pmt_variance_values = np.load("data/pmt_variance_values.npy")
x_coords = np.load("data/x_coords.npy")
y_coords = np.load("data/y_coords.npy")


#Global constants
NUM_EVENTS, TEL_PIXEL_COUNT = np.shape(events_array)




mean_x = np.zeros(2500)
mean_x2 = np.zeros(2500)
mean_y = np.zeros(2500)
mean_y2 = np.zeros(2500)
mean_xy = np.zeros(2500)

sigma_x2 = np.zeros(2500)
sigma_y2 = np.zeros(2500)
sigma_xy = np.zeros(2500)


image_d = np.zeros(2500)
image_z = np.zeros(2500)
image_u = np.zeros(2500)
image_v = np.zeros(2500)

mean_image_length2 = np.zeros(2500)
mean_image_width2 = np.zeros(2500)
mean_image_distance2 = np.zeros(2500)
mean_image_azwidth2 = np.zeros(2500)
mean_image_miss2 = np.zeros(2500)

alpha = np.zeros(2500)








for i, event in enumerate(cherenkov_array):
    #if i == 10:
        #break
    sum_sig = np.sum(event)
    sum_sig_x = 0
    sum_sig_x2 = 0
    sum_sig_y = 0
    sum_sig_y2 = 0
    sum_sig_xy = 0


    if sum_sig == 0:    # i.e. No signal for this event.
        continue        # Ends the current iteration of the for loop.

    for i_phototube in range(TEL_PIXEL_COUNT):
        sum_sig_x += event[i_phototube] * x_coords[i_phototube]
        sum_sig_x2 += event[i_phototube] * (x_coords[i_phototube] ** 2)

        sum_sig_y += event[i_phototube] * y_coords[i_phototube]
        sum_sig_y2 += event[i_phototube] * (y_coords[i_phototube] ** 2)

        sum_sig_xy += event[i_phototube] * x_coords[i_phototube] * y_coords[i_phototube]

    mean_x[i] = sum_sig_x / sum_sig
    mean_x2[i] = sum_sig_x2 / sum_sig

    mean_y[i] = sum_sig_y / sum_sig
    mean_y2[i] = sum_sig_y2 / sum_sig

    mean_xy[i] = sum_sig_xy / sum_sig

    sigma_x2[i] = mean_x2[i] - (mean_x[i] ** 2)
    sigma_y2[i] = mean_y2[i] - (mean_y[i] ** 2)
    sigma_xy[i] = mean_xy[i] - (mean_x[i] * mean_y[i])


    image_d[i] = sigma_y2[i] - sigma_x2[i]
    image_z[i] = ( (image_d[i]**2) + (4*(sigma_xy[i] ** 2)) ) ** 0.5
    image_u[i] = 1 + ( image_d[i] / image_z[i] )
    image_v[i] = 2- image_u[i]

    mean_image_length2[i] = (sigma_x2[i] +sigma_y2[i] + image_z[i]) / 2
    mean_image_width2[i] = (sigma_x2[i] +sigma_y2[i] - image_z[i]) / 2
    mean_image_distance2[i] = (mean_x[i] ** 2) + (mean_y[i] ** 2)
    mean_image_azwidth2[i] = (((mean_x[i] **2) * mean_y2[i]) - (2 * mean_x[i] * mean_y[i] * mean_xy[i]) + (mean_x2[i] * (mean_y[i] ** 2))  ) / mean_image_distance2[i]
    mean_image_miss2[i] =( ((image_u[i] * (mean_x[i] ** 2) ) + (image_v[i] * (mean_y[i] ** 2)) ) / 2 ) - ((2 * sigma_xy[i] * mean_x[i] * mean_y[i]) / image_z[i])
    alpha[i] = np.arcsin( (mean_image_miss2[i] / mean_image_distance2[i]) ** 0.5 )


#for i in range(10):
    #print("<x_{0}> = {1:0.4}".format(i, mean_x[i]))
    #print("<x2_{0}> = {1:0.4}".format(i, mean_x2[i]))
    #print("<y_{0}> = {1:0.4}".format(i, mean_y[i]))
    #print("<y2_{0}> = {1:0.4}".format(i, mean_y2[i]))
    #print("<xy_{0}> = {1:0.4}".format(i, mean_xy[i]))
    #print("\u03C3_x2{0} = {1:0.4}".format(i, sigma_x2[i]))
    #print("\u03C3_y2{0} = {1:0.4}".format(i, sigma_y2[i]))
    #print("\u03C3_xy{0} = {1:0.4}".format(i, sigma_xy[i]))
    #print("\u03B1_{0} = {1:0.4}".format(i, alpha[i]))

    #print()







np.save("data/parameters/mean_x.npy", mean_x)
np.save("data/parameters/mean_x2.npy", mean_x2)
np.save("data/parameters/mean_y.npy", mean_y)
np.save("data/parameters/mean_y2.npy", mean_y2)
np.save("data/parameters/mean_xy.npy", mean_xy)

np.save("data/parameters/sigma_x2.npy", sigma_x2)
np.save("data/parameters/sigma_y2.npy", sigma_y2)
np.save("data/parameters/sigma_xy.npy", sigma_xy)


np.save("data/parameters/image_d.npy", image_d)
np.save("data/parameters/image_z.npy", image_z)
np.save("data/parameters/image_u.npy", image_u)
np.save("data/parameters/image_v.npy", image_v)

np.save("data/parameters/mean_image_length2.npy", mean_image_length2)
np.save("data/parameters/mean_image_width2.npy", mean_image_width2)
np.save("data/parameters/mean_image_distance2.npy", mean_image_distance2)
np.save("data/parameters/mean_image_azwidth2.npy", mean_image_azwidth2)
np.save("data/parameters/mean_image_miss2.npy", mean_image_miss2)

np.save("data/parameters/alpha.npy", alpha)



