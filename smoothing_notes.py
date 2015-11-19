#### smoothing notes

from scipy.io.idl import readsav
from astropy.convolution import convolve, Box1DKernel


filepath='/Users/cealexan/Dropbox/python_work/cherry_struc.sav'
s=readsav(filepath)

data=s.cut2
hic=s.cut
X=np.linspace(0, 54,55)
X2=np.linspace(0, 56,57)
X4=np.linspace(0, 58,59)
X8=np.linspace(0, 62,63)
X12=np.linspace(0, 66,67)


smooth_hic2 = convolve(hic, Box1DKernel(2))
smooth_hic4 = convolve(hic, Box1DKernel(4))
smooth_hic8 = convolve(hic, Box1DKernel(8))
smooth_hic12 = convolve(hic, Box1DKernel(12))




#smooth_aia = convolve(aia, Box1DKernel(11))





plt.figure()
plt.plot(X, hic, color = 'black', label = 'Noisy data',linewidth=2)
plt.plot(X, smooth_hic2[1:-1], color = 'r', label = 'smooth 2')
plt.plot(X, smooth_hic4[2:-2], color = 'g', label = 'smooth 4')
plt.plot(X, smooth_hic8[4:-4], color = 'b', label = 'smooth 8')
plt.plot(X, smooth_hic12[6:-6], color = 'c', label = 'smooth 12')
plt.ylim(450,620)
plt.legend(loc = 'best', frameon = False)
plt.xlim(5,50)


plt.xlabel('Some points along X', fontsize = 16)
plt.ylabel('Data', fontsize = 16)
plt.title(r'smoothing data', fontsize = 16)  
plt.legend(loc = 2, frameon = False)
#plt.text(10,750,'FWHM = '+ str(round(FWHM,2)), fontdict=font)
plt.grid(True)
plt.show()
   
   
