#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:13:00 2020

@author: cormac
"""


import matplotlib.pyplot as plt
import numpy as np




main_data = np.arange(10)



# Figure
fig, ax1 = plt.subplots()


# Labels
ax1.set_xlabel('Main Data Variable')
ax1.set_ylabel('Main Data Function')
ax1.set_title('Our Main Experiment')

# c sequence
c = np.clip(main_data, 4, 6)
for i in range(10):
    if main_data[i] > 7:
        plt.text(main_data[i], main_data[i], i)

# Plot
plt.scatter( main_data, main_data, c=c, cmap='magma' )
cbar = plt.colorbar()
cbar.set_label('Color Intensity')


#plt.plot(main_data, main_data, cmap='magma', marker='h')
plt.show()
