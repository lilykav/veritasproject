#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:02:23 2020

@author: cormac
"""

#Importing All of the relevant modules
import matplotlib.pyplot as plt
import numpy as np



class PMPIX():

    def __init__(self, tele_id, pix_id, pix_shape, angle, x_pos, y_pos, pmt_radius, geom_eff, quant_eff, sig_fluct, sig_rize, sig_fall, rc_coupling, belong_bol, anal_bol, time_offset, gain_factor):

        self.tele_id = tele_id          # the telescope identification number
        self.pix_id = pix_id            # the pixel identification number
        self.pix_shape = pix_shape      # the pixel shape ( 1=circular, 2=hexangonal, 3=square )
        self.angle = angle              # Orientation angle in degrees ( relastivie to x-axis )
        self.x_pos = x_pos              # x coordinate of pixel in mm (plane is looking in direaction of telescope)
        self.y_pos = y_pos              # y coordinate of pixel in mm (telescope points south, +x goes W, +y goes Up in sky)
        self.pmt_radius = pmt_radius    # Radius of Photomultiplier tube in mm (Sensitivity area)
        self.geom_eff = geom_eff        # Geometrical efficency, such as effects of light cone loss
        self.quant_eff = quant_eff      # Quantum efficiency identification number to be used for that tube
        self.sig_fluct = sig_fluct      # The single photoelectron signal relative amplitude fluctuation
        self.sig_rize = sig_rize        # The signal rize time in nanosecondes
        self.sig_fall = sig_fall        # The signal fall time  in nanosecondes
        self.rc_coupling = rc_coupling  # The RC coupling time constant in nanosecondes
        self.belong_bol = belong_bol    # The bellongin of the channel to the trigger ( 1 if it bellongs, 0 otherwise )
        self.anal_bol = anal_bol        # Pixel flag whether it is for analysis or not
        self.time_offset = time_offset  # Time offset in nanoseconds
        self.gain_factor = gain_factor  # A relative gain factor to account for the imperfect gain flat fielding ( in analysis pixel number mult by gain, in simulation pulse amplitudes divided by this )




    def print_pos(self):
        print(self.x_pos, self.y_pos)



PMPIX1= PMPIX(1, 1, 1, 0.0, 0.00, 0.00, 14.0, 1.00, 1, 0.44, 4.0, 65.0, 0.000, 1, 1, 0.0, 1.0)



PMPIX1.print_pos()

read_PMT_info = open("PMTS_info.txt", "r")
contents = read_PMT_info.read()
new = contents.split("\n")
del new[-1]


x_array = np.zeros(len(new))
y_array = np.zeros(len(new))


for i in range(len(new)):
    # j = new[i].partition(" ")[2]
    new[i] = new[i].split()
    new[i][0] = new[i][0] + new[i][1] + "_" + new[i][2]
    del new[i][1:3]
    #print(new[i])
    x_array[i] = new[i][3]
    y_array[i] = new[i][4]

    if i==25 or i==26:
        pix_col='red'
    else:
        pix_col='grey'
    plt.plot(x_array[i], y_array[i], 'h', color=pix_col, markersize=8)
    #plt.text(x_array[i], y_array[i], i)   # Adds pixel number to plot



plt.title("PMPIX")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#plt.plot(x_array, y_array, 'h', color='grey')
#plt.show()





