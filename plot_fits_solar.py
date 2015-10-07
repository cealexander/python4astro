import astropy.io.fits as fits

fname='/Users/cealexan/Documents/work/projects/NRLvsOBS/aia.lev1.171A_2010-12-11T02_24_00.34Z.image_lev1.fits'
fits.getheader(fname)

header=fits.getheader(fname)

header['CDELT2']

data=fits.open(fname)
data[0].header
image = data[0].data
image.shape

plt.imshow(image)
plt.show()


f=plt.figure()
plt.imshow(image,cmap=plt.cm.hsv)





import astropy.units as u
fig = plt.figure()
plt.imshow(image,cmap=plt.cm.afmhot, vmin=0,vmax=1500)
plt.colorbar()
plt.show()

