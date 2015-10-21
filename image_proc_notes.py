from scipy import ndimage
import matplotlib.pyplot as plt
from scipy import misc
import astropy.io.fits as fits

fname='/Users/cealexan/Documents/work/projects/NRLvsOBS/aia.lev1.171A_2010-12-11T02_24_00.34Z.image_lev1.fits'
data=fits.open(fname)
image = data[0].data

#other way to do it
image=fits.getdata(fname)
plt.imshow(image, cmap=plt.cm.ocean)        


#Increase contrast by setting min and max values:
print image.max()
print image.min()

plt.imshow(image, cmap=plt.cm.gray, vmin=0, vmax=1500)        

# Remove axes and ticks
plt.axis('off')

plt.contour(image, [60, 211])      

plt.imshow(image[2500:3500, 2500:3500], cmap=plt.cm.gray)        

plt.imshow(image[2500:3500, 2500:3500], cmap=plt.cm.gray, interpolation='nearest')        


######################## using lena image


lena = misc.lena()
lena[0, 40]

# Slicing
lena[10:13, 20:23]



lena[100:120] = 255

lx, ly = lena.shape
X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4
# Masks
lena[mask] = 0

# Fancy indexing - draws a black line
lena[range(400), range(400)] = 255

plt.imshow(lena,cmap=plt.cm.gray)
plt.show()

#make empty plot space
plt.plot([128,128],[128,384], color='blue',linewidth=1)
plt.plot([384,384],[128,384], color='blue',linewidth=1)
plt.plot([128,384],[128,128], color='blue',linewidth=1)
plt.plot([128,384],[384,384], color='blue',linewidth=1)




####### rotate image

lena = misc.lena()
lx, ly = lena.shape
# Cropping
crop_lena = lena[lx / 4: - lx / 4, ly / 4: - ly / 4]
plt.imshow(crop_lena,cmap=plt.cm.gray)

# up <-> down flip
flip_ud_lena = np.flipud(lena)
plt.imshow(flip_ud_lena,cmap=plt.cm.gray)

# rotation
rotate_lena = ndimage.rotate(lena, 45)
rotate_lena_noreshape = ndimage.rotate(lena, 45, reshape=False)

#fits in whole pic
plt.imshow(rotate_lena,cmap=plt.cm.gray)

#keeps whole area same as image size
plt.imshow(rotate_lena_noreshape,cmap=plt.cm.gray)


# FILTERING


from scipy import misc
lena = misc.lena()
blurred_lena = ndimage.gaussian_filter(lena, sigma=3)
very_blurred = ndimage.gaussian_filter(lena, sigma=5)


plt.imshow(blurred_lena,cmap=plt.cm.gray)
plt.imshow(very_blurred,cmap=plt.cm.gray)

local_mean = ndimage.uniform_filter(lena, size=11)

plt.imshow(local_mean,cmap=plt.cm.gray)

##Sharpen a blurred image:

from scipy import misc
lena = misc.lena()
blurred_l = ndimage.gaussian_filter(lena, 3)
plt.imshow(blurred_l,cmap=plt.cm.gray)

#increase the weight of edges by adding an approximation of the Laplacian:
filter_blurred_l = ndimage.gaussian_filter(blurred_l, 1)
alpha = 30
sharpened = blurred_l + alpha * (blurred_l - filter_blurred_l)
plt.imshow(sharpened,cmap=plt.cm.gray)



########################################################
import numpy as np
import scipy
from scipy import ndimage
import matplotlib.pyplot as plt

l = scipy.misc.lena()
l = l[230:290, 220:320]

noisy = l + 0.4*l.std()*np.random.random(l.shape)

gauss_denoised = ndimage.gaussian_filter(noisy, 2)
med_denoised = ndimage.median_filter(noisy, 3)


plt.figure(figsize=(12,2.8))

plt.subplot(131)
plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('noisy', fontsize=20)
plt.subplot(132)
plt.imshow(gauss_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('Gaussian filter', fontsize=20)
plt.subplot(133)
plt.imshow(med_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('Median filter', fontsize=20)

plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,
                    right=1)
plt.show()
