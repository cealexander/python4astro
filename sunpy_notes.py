#to tell you where it downloads files to
import sunpy
sunpy.print_config()

#download files
import sunpy.data
sunpy.data.download_sample_data()

import sys,os
import glob
fdir ='/Users/cealexan/sunpy/data/sample_data/'
filenames=sorted(glob.glob(fdir + '*.fits'))
for file in filenames:
    print os.path.basename(file)

filename=filenames[1]


import sunpy.data.sample
import sunpy.map
aia = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
smap = aia.submap([-1200,-200]*u.arcsec,[-1000,-0]*u.arcsec)
smap.peek(draw_grid=True)
aia.peek()


import astropy.units as u
import sunpy.map
import sunpy.data
#sunpy.data.download_sample_data(overwrite=False)   
import sunpy.data.sample
aia = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
aia.submap([-5,5]*u.arcsec, [-5,5]*u.arcsec)   




import sunpy.map
import matplotlib.pyplot as plt
import sunpy.data.sample
aia = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)
fig = plt.figure()
ax = plt.subplot(112)
aia.plot()
aia.draw_limb()
aia.draw_grid()
#plt.colorbar()
aia.draw_limb()
plt.show()



import numpy as np
import sunpy.data.sample
from sunpy.lightcurve import LightCurve
times = np.arange(1000) * 2.0
signal = np.sin(np.arange(1000)*0.02 ) + np.random.random(1000)
light_curve = LightCurve.create({"signal": signal},index = times)
light_curve.peek()