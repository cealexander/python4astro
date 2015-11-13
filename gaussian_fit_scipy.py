import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from datetime import datetime




def gaussian(x, amp, mu, sigma):

    return amp*np.exp(-(x-mu)**2/(2.0*sigma**2))
    
    

if __name__ == '__main__':
    
    # Start time
    st_time = datetime.now()
    
    # Generate data with noise
    np.random.seed(0)
    X = np.linspace(-15, 15, 200)
    X0 = 0.0
    AMP = 1.0
    SIGMA = 3.0
    
    data = AMP*np.exp(-(X - X0)**2.0/(2.0*SIGMA**2.0)) + np.random.normal(0.0, 0.2, X.shape)
    
    # Initial guess of parameters
    p0 = [AMP, X0, SIGMA]
    
    # Perform fit
    coeff, var_matrix = curve_fit(gaussian, X, data, p0 = p0)
    print coeff
    
    # Compute fit with parameters
    G = gaussian(X, coeff[0], coeff[1], coeff[2])
    FWHM=2.35*coeff[2]
    
    # Plot data with fit
    plt.figure()
    plt.scatter(X, data, color = 'purple', label = 'Noisy data')
    plt.plot(X, G, color = 'cyan', label = 'Fit')
    plt.xlabel('Some points along X', fontsize = 16)
    plt.ylabel('Data', fontsize = 16)
    plt.title(r'Gaussian fit with SciPy $\alpha$', fontsize = 16)  
    plt.legend(loc = 2, frameon = False)
    plt.text(0,-0.5,'FWHM = '+ str(round(FWHM,2)))
    plt.grid(True)
    plt.show()
    
    print
    print 'Run time: ', datetime.now() - st_time