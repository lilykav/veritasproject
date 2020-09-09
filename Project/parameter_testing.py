#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 9 11:35:15 2020

@author: cormac
"""

import numpy as np
import matplotlib.pyplot as plt


np.set_printoptions(threshold=np.inf)



# Array importing
events_array = np.load("data/events_array.npy")
cherenkov_array = np.load("data/cherenkov_array.npy")
#pmt_array = np.load("data/pmt_array.npy")
#pmt_peak_freq = np.load("data/pmt_peak_freq.npy")
#pmt_mean_values = np.load("data/pmt_mean_values.npy")
#pmt_variance_values = np.load("data/pmt_variance_values.npy")
x_coords = np.load("data/x_coords.npy")
y_coords = np.load("data/y_coords.npy")



mean_x = np.load("data/parameters/mean_x.npy")
mean_x2 = np.load("data/parameters/mean_x2.npy")
mean_y = np.load("data/parameters/mean_y.npy")
mean_y2 = np.load("data/parameters/mean_y2.npy")
mean_xy = np.load("data/parameters/mean_xy.npy")

sigma_x2 = np.load("data/parameters/sigma_x2.npy")
sigma_y2 = np.load("data/parameters/sigma_y2.npy")
sigma_xy = np.load("data/parameters/sigma_xy.npy")


image_d = np.load("data/parameters/image_d.npy")
image_z = np.load("data/parameters/image_z.npy")
image_u = np.load("data/parameters/image_u.npy")
image_v = np.load("data/parameters/image_v.npy")

mean_image_length2 = np.load("data/parameters/mean_image_length2.npy")
mean_image_width2 = np.load("data/parameters/mean_image_width2.npy")
mean_image_distance2 = np.load("data/parameters/mean_image_distance2.npy")
mean_image_azwidth2 = np.load("data/parameters/mean_image_azwidth2.npy")
mean_image_miss2 = np.load("data/parameters/mean_image_miss2.npy")

alpha = np.load("data/parameters/alpha.npy")



print(alpha)
