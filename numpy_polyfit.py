import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sys



X = np.linspace(0,10,100)

# Line
# slope, y intercept
m = 0.5
b = 5

# Generate data with noise
np.random.seed(0)
lin_data = m*X + b + np.random.normal(0.0, 0.2, X.shape)

# Perform fit
lin_fit = np.polyfit(X,lin_data, 1)

# Polynomial
# Coeffs
A = 4.0
B = 0.5
C = 2

# Generate data with noise
poly_data = A*(X+np.random.normal(0.0, 2.0, X.shape))**2 + B*X + C 

# Perform fitting
poly_fit = np.polyfit(X, poly_data, 2)


# Find roots
rts = np.roots([A,B,C])
print rts

# Plot data with fits
plt.figure()
plt.scatter(X, lin_data, color = 'orange', label = 'Noisy data')
plt.plot(X, lin_fit[0]*X + lin_fit[1], color = 'cyan', label = 'Fit')
plt.xlabel('Some points along X', fontsize = 16)
plt.ylabel('Data', fontsize = 16)
plt.title(r'Linear Fit', fontsize = 16)  
plt.legend(loc = 2, frameon = False)
plt.grid(True)
plt.show()

plt.figure()
plt.scatter(X, poly_data, color = 'b', label = 'Noisy data')
plt.plot(X, poly_fit[0]*X**2 + poly_fit[1]*X + poly_fit[2], color = 'g', label = 'Fit')
plt.xlabel('Some points along X', fontsize = 16)
plt.ylabel('Data', fontsize = 16)
plt.title(r'Linear Fit', fontsize = 16)  
plt.legend(loc = 2, frameon = False)
plt.grid(True)
plt.show()