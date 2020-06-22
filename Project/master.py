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

# Global Constants
N_EVENTS = 2500
TEL_PIXEL_COUNT = len(tel_details)


x_coords = np.zeros(TEL_PIXEL_COUNT)
y_coords = np.zeros(TEL_PIXEL_COUNT)
for i in range(TEL_PIXEL_COUNT):
    # Gets the telescope Details and coordinates for pixels, and plots them according to PixelDetection

    # j = tel_details[i].partition(" ")[2]

    tel_details[i] = tel_details[i].split()
    tel_details[i][0] = tel_details[i][0] + tel_details[i][1] + "_" + tel_details[i][2]
    del tel_details[i][1:3]
    x_coords[i] = tel_details[i][3]
    y_coords[i] = tel_details[i][4]

#print(tel_details[12])


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
pmt_array = np.transpose(events_array)



def PulseHeightSpectrum(pmt):
    for count, element in enumerate(pmt):
        plt.hist(element, bins=np.arange(30, element.max()+1))



        plt.savefig('output/pulse_spectrum/output_pulse_spectrumt_{0}.png'.format(count + 1), bbox_inches='tight')

PulseHeightSpectrum(pmt_array)



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
    fig.savefig('output/output_plot_event_{0}.pdf'.format(index + 1), bbox_inches='tight')






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
    TelescopePlot(element, count)
    #exit()
