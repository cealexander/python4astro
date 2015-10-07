# -*- coding: utf-8 -*-


import math
import numpy as np
import scipy as sp  # must import system last, allows you to change directories within the script
import matplotlib.pyplot as plt     #pyplot most commonly used
import sys,os      #allows you to stop…sys.exit ()  ;equivlene t to idl stop              

#===========================================================
# plotting
#===========================================================
plt.figure()  # get a window
fontP=FontProperties()
fontP.set_size('medium')

x=arange(0,10)
y=numpy.sin(x)
#plt.plot(x,y,label='thing $\AA$')

plt.plot(x, y, label = 'first_'+r' $\AA$')
plt.plot(x-5, y, label = 'second_'+r' $\AA$')

# Plot properites 
plt.xlabel('x', fontsize = 20)
plt.ylabel(r'Fake units [mm$^{2}$]', fontsize = 20)
plt.title('Amazing graph!')
plt.legend(loc = 'best', frameon = False)
plt.grid(True)
plt.tick_params(labelsize = 14)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))  # Scientific notation along y-axis

plt.show()





#===========================================================
# plotting
#===========================================================

# look up transparent background color
plt.figure(figsize=(15,10))  # opens a window, size in inches


plt.plot(z)

plt.savefig



fig1=plt.figure()
ax1=fig1.add_subplot() # look up args
fig2=plt.figure()
ax2=fig2.add_subplot()



L=[x**2 for x in range(0,10)]

# Defines a new figure (window) 
plt.figure()

# FontProperties is a module
fontP = FontProperties()
fontP.set_size('medium')

# Line plots graphed in the defined figure (analagous to oplot in IDL)
plt.plot(alpha_b4c, A_eff_b4c[0], label = str(WL[0])+r' $\AA$')
plt.plot(alpha_b4c, A_eff_b4c[1], label = str(WL[1])+r' $\AA$')
plt.plot(alpha_b4c, A_eff_b4c[2], label = str(WL[2])+r' $\AA$')
plt.plot(alpha_b4c, A_eff_b4c[3], label = str(WL[3])+r' $\AA$')
plt.plot(alpha_b4c, A_eff_b4c[4], label = str(WL[4])+r' $\AA$')
plt.plot(alpha_b4c, A_eff_b4c[5], label = str(WL[5])+r' $\AA$')
plt.plot(alpha_b4c, A_eff_b4c[6], label = str(WL[6])+r' $\AA$')

# Plot properites 
plt.xlabel('Graze Angle [degrees]', fontsize = 20)
plt.ylabel(r'Effective Area [mm$^{2}$]', fontsize = 20)
plt.title('MaGIXS Effective Area')
plt.legend(loc = 'best', frameon = False)
plt.grid(True)
plt.tick_params(labelsize = 14)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))  # Scientific notation along y-axis

# How to save a figure...
plt.savefig('C:\\Users\\pchampey\\Documents\\MSFC_SRT\\MaGIXS\\a_eff_b4c_full_band.png')

# Display the plot (must be after savefig, if before, figure will be empty window)
plt.show()











#Plots

Plt.figure()   #..define a window,,,can format the window size etc

frontP.Fontproperite()  change font size

#overplot the same 
plt.plot(alpha…
plot..

plot.scatter, label ….can   use latex  precede define +r ‘ $\AA$’

or it can pick the best area automoacticly
font size or colors,etc. til
grid, 





from matplotlib.font_manager import FontProperties

plt.figure.............

fontP=FontProperties()
fontP.set_size('medium')

#add extra things here
plt.ticklable_format(style='sci',axis='y',scilimits=(0,0))








