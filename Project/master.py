#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:02:23 2020

@author: cormac
"""

# Importing All of the relevant modules
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(threshold=np.inf)




# Global Constants
N_EVENTS = 2500
TEL_PIXEL_COUNT = 499









# For Now this class is not used. Leaving it here for further use.
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


# Test for class
PMPIX1= PMPIX(1, 1, 1, 0.0, 0.00, 0.00, 14.0, 1.00, 1, 0.44, 4.0, 65.0, 0.000, 1, 1, 0.0, 1.0)









# Reading our Telescope data
read_tel_details = open("data/PMTS_info.txt", "r")
pmts_info = read_tel_details.read()
tel_details = pmts_info.splitlines()


# Reading our Event data
read_event_details = open("data/gamsims_2500.dat")
gamsims = read_event_details.read()
events = gamsims.splitlines(0)


# Restructures Data into a 2D Array[ [event_1] [event_2] ... ] with [ pix_1_val pix_2_val ... ]
events_array = np.zeros((2500, 499))
for count, element in enumerate(events):
    element = element.split()
    events_array[int(element[0]) - 1][int(element[1]) - 1] = int(element[2])

#print(events_array)






def PixelDetection(pix_num):
    if pix_num >= 20:
        return 'blue'
    else:
        return 'grey'





def TelescopePlot(current_event, index):

    x_array = np.zeros(len(tel_details))
    y_array = np.zeros(len(tel_details))

    for i in range(len(tel_details)):
        # Gets the telescope Details and coordinates for pixels, and plots them according to PixelDetection

        # j = tel_details[i].partition(" ")[2]

        tel_details[i] = tel_details[i].split()
        tel_details[i][0] = tel_details[i][0] + tel_details[i][1] + "_" + tel_details[i][2]
        del tel_details[i][1:3]
        #print(tel_details[i])
        x_array[i] = tel_details[i][3]
        y_array[i] = tel_details[i][4]


        pix_col=PixelDetection(current_event[i])


        plt.plot(x_array[i], y_array[i], 'h', color=pix_col, markersize=8)
        #plt.text(x_array[i], y_array[i], i)   # Adds pixel number to plot





    # Finishing the Plot for the telescope
    plt.title("PMPIX")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig('output/output_plot_event_{0}.pdf'.format(index + 1), bbox_inches='tight')




for count, element in enumerate(events_array):
    TelescopePlot(element, count)
    print(count)
    print(element)
    exit()
