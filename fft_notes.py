import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

N = 100
x = np.linspace(0,2*np.pi,N)
y = np.sin(x) + np.random.random(N) * 0.2

w = scipy.fftpack.rfft(y)
f = scipy.fftpack.rfftfreq(N, x[1]-x[0])
spectrum = w**2

cutoff_idx = spectrum < (spectrum.max()/5)
w2 = w.copy()
w2[cutoff_idx] = 0

y2 = scipy.fftpack.irfft(w2)

plt.figure()
plt.plot(x,y)
plt.plot(x,y2)
plt.show()


from scipy.io.idl import readsav

filepath='/Users/cealexan/Dropbox/python_work/cherry_struc.sav'
s=readsav(filepath)

aia=s.cut2
hic=s.cut
   
XX=np.linspace(0, 54,55)

from scipy import interpolate

#### aia

w = scipy.fftpack.rfft(aia)
f = scipy.fftpack.rfftfreq(55, XX[1]-XX[0])
spectrum = w**2
cutoff_idx = spectrum < (spectrum.max()/5)
w2 = w.copy()
w2[cutoff_idx] = 0
y2 = scipy.fftpack.irfft(w2)

plt.figure()
plt.plot(X,aia)
plt.plot(X,y2)
plt.show()

