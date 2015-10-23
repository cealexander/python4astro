import numpy as np
from astropy.modeling import models, fitting
import matplotlib.pyplot as plt
from datetime import datetime
import sys



    
st_time = datetime.now()
 
# Gereate data with noise     
np.random.seed(0)
X = np.linspace(-15, 15, 200)
X0 = 0.0
AMP = 1.0
SIGMA = 3.0
data1 = AMP*np.exp(-(X - X0)**2.0/(2.0*SIGMA**2.0))   
data = AMP*np.exp(-(X - X0)**2.0/(2.0*SIGMA**2.0)) + np.random.normal(0.0, 0.2, X.shape)

##CEA added
plt.figure()
plt.scatter(X,data,marker='o')
plt.plot(X,data1,color='blue')
##
   
     
# Call 1D Gaussian function 
g_init = models.Gaussian1D(amplitude = 1.0, mean = 0, stddev = 3.0) 

# Define fitting method
fit_g = fitting.LevMarLSQFitter()

# Perform fitting    
g = fit_g(g_init, X, data)   
print g

##CEA added
amp_new=g.amplitude[0]
mean_new=g.mean[0]
sdv_new=g.stddev[0]
##

    
# Plot data with fit            
plt.figure()
plt.scatter(X, data, color = 'purple', label = 'Noisy data')
plt.plot(X, g(X), color = 'cyan', label = 'Fit')
plt.xlabel('Some points along X', fontsize = 16)
plt.ylabel('Data', fontsize = 16)
plt.title(r'Gaussian fit with AstroPy', fontsize = 16)  
plt.legend(loc = 2, frameon = False)
plt.grid(True)
plt.show()
    