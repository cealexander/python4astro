import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from datetime import datetime
import sys,os 

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


def gaussian(x, amp, mu, sigma):

    return amp*np.exp(-(x-mu)**2/(2.0*sigma**2))
    
    

if __name__ == '__main__':
    
    # Start time
    st_time = datetime.now()
    

    from scipy.io.idl import readsav

    filepath='/Users/cealexan/Dropbox/python_work/cherry_struc.sav'
    s=readsav(filepath)

    data=s.cut2
    hic=s.cut
    
    
    X=np.linspace(0, 54,55)

    X0 = 0.0
    AMP = 1.0
    SIGMA = 3.0
     
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
    plt.plot(X, data, color = 'purple', label = 'Noisy data')
    plt.plot(X, G, color = 'cyan', label = 'Fit')
    plt.xlabel('Some points along X', fontsize = 16)
    plt.ylabel('Data', fontsize = 16)
    plt.title(r'Gaussian fit with SciPy', fontsize = 16)  
    plt.legend(loc = 2, frameon = False)
    plt.text(10,750,'FWHM = '+ str(round(FWHM,2)), fontdict=font)
    plt.grid(True)
    plt.show()
    
    sys.exit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    coeff, var_matrix = curve_fit(gaussian, X, hic, p0 = p0)
    print coeff
    
    # Compute fit with parameters
    G = gaussian(X, coeff[0], coeff[1], coeff[2])
    FWHM=2.35*coeff[2]
    
    # Plot data with fit
    plt.figure()
    plt.plot(X, hic, color = 'purple', label = 'Noisy data')
    plt.plot(X, G, color = 'cyan', label = 'Fit')
    plt.xlabel('Some points along X', fontsize = 16)
    plt.ylabel('Data', fontsize = 16)
    plt.title(r'Gaussian fit with SciPy', fontsize = 16)  
    plt.legend(loc = 2, frameon = False)
    
    plt.grid(True)
    plt.show()
    #plt.close('all')
    
    
    
    
    #sys.exit()
    #######################
    
    hic1=hic[10:25]
    hic2=hic[24:40]
    x1=X[10:25]
    x2=X[24:40]
    p0 = [200, 2.0, 0.02]
    coeff, var_matrix = curve_fit(gaussian, x1, hic1, p0 = p0)
    print coeff
    G1 = gaussian(x1, coeff[0], coeff[1], coeff[2])
   
    p0 = [200, 2.0, 0.03]
    coeff, var_matrix = curve_fit(gaussian, x2, hic2, p0 = p0)
    print coeff
    G2 = gaussian(x2, coeff[0], coeff[1], coeff[2])
   
    # Plot data with fit
    plt.figure()
    plt.plot(X, hic, color = 'purple', label = 'Noisy data')
    plt.plot(X[10:25],hic[10:25],color='red')
    plt.plot(X[24:40],hic[24:40],color='green')
    plt.plot(x1, G1, color = 'cyan', label = 'Fit 1')
    plt.plot(x2, G2, color = 'orange', label = 'Fit 2')
    plt.xlabel('Some points along X', fontsize = 16)
    plt.ylabel('Data', fontsize = 16)
    plt.title(r'Gaussian fit with SciPy', fontsize = 16)  
    plt.legend(loc = 2, frameon = False)
    plt.grid(True)
    plt.show()
    
    print
    print 'Run time: ', datetime.now() - st_time