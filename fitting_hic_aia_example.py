import numpy as np
import matplotlib.pyplot as plt

from scipy.io.idl import readsav

filepath='/Users/cealexan/Dropbox/python_work/cherry_struc.sav'
s=readsav(filepath)

#hic=np.pad(s.cut,15,mode='minimum')
#aia=np.pad(s.cut2,15,mode='minimum')
aia=s.cut2
hic=s.cut

plt.figure(figsize=(23/2,15/2), dpi=80)
# Create a new subplot from a grid of 1x1  (row, column, plot#)
plt.subplot(121)
plt.plot(hic, color='blue',linewidth=1)
plt.title('Hi-C')
plt.subplot(122)
plt.plot(aia, color='blue',linewidth=1)
plt.title('AIA')

plt.show()

#X=np.linspace(0, 84,85)
X=np.linspace(0, 54,55)

# Call 1D Gaussian function 
g_init = models.Gaussian1D(amplitude = 1.0, mean = 0, stddev = 3.0) 

# Define fitting method
fit_g = fitting.LevMarLSQFitter()

# Perform fitting    
g = fit_g(g_init, X, hic)   

# Plot data with fit            
plt.figure()
plt.plot(X, hic, color = 'purple', label = 'AIA data')
plt.plot(X, g(X), color = 'cyan', label = 'Fit')
plt.xlabel('Some points along X', fontsize = 16)
plt.ylabel('Data', fontsize = 16)
plt.title(r'Gaussian fit with AstroPy', fontsize = 16)  
plt.legend(loc = 2, frameon = False)
plt.grid(True)
plt.show()

##############################################

XX=np.linspace(20, 60,85)

# Call 1D Gaussian function 
g_init = models.Gaussian1D(amplitude = 940.0, mean = 0, stddev = 3.0) 

# Define fitting method
fit_g = fitting.LevMarLSQFitter()

# Perform fitting    
gg = fit_g(g_init, XX, aia)   

gg.amplitude = 945.0
gg.stddev=30.0
# Plot data with fit            
plt.figure()
plt.plot(X, aia, color = 'purple', label = 'AIA data')
plt.plot(X, g(X), color = 'cyan', label = 'Fit1')
plt.plot(XX, gg(XX), color = 'black', label = 'Fit2')

plt.xlabel('Some points along X', fontsize = 16)
plt.ylabel('Data', fontsize = 16)
plt.title(r'Gaussian fit with AstroPy', fontsize = 16)  
plt.legend(loc = 2, frameon = False)
plt.grid(True)
plt.show()

################################
plt.figure()
plt.plot(X,hic)

plt.plot(X[10:25],hic[10:25],color='red')
plt.plot(X[24:40],hic[24:40],color='green')

hic1=hic[10:25]
hic2=hic[24:40]
x1=X[10:25]
x2=X[24:40]

g_init = models.Gaussian1D(amplitude = 1.0, mean = 0, stddev = 3.0) 
fit_g = fitting.LevMarLSQFitter()
g1 = fit_g(g_init, x1, hic1)   

g_init = models.Gaussian1D(amplitude = 600.0, mean = 0, stddev = 3.0) 
fit_g = fitting.LevMarLSQFitter()
g2 = fit_g(g_init, x2, hic2)   


plt.figure()
plt.plot(X,hic)
plt.plot(x1,hic1,color='red')
plt.plot(x2,hic2,color='green')
plt.plot(x1, g1(x1), color = 'cyan', label = 'Fit1')
plt.plot(x2, g2(x2), color = 'cyan', label = 'Fit2')
plt.xlabel('Some points along X', fontsize = 16)
plt.ylabel('Data', fontsize = 16)
plt.title(r'Hi-C fit gaussian with astropy', fontsize = 16)  
plt.legend(loc = 2, frameon = False)
plt.grid(True)
plt.show()
