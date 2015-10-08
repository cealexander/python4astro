from scipy import misc
l = misc.lena()
misc.imsave('lena.png', l) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(l)
plt.show()




l = misc.lena()
import matplotlib.pyplot as plt
plt.imshow(l, cmap=plt.cm.ocean)        


#Increase contrast by setting min and max values:

plt.imshow(l, cmap=plt.cm.gray, vmin=30, vmax=200)        

# Remove axes and ticks
plt.axis('off')

plt.contour(l, [60, 211])      

plt.imshow(l[200:220, 200:220], cmap=plt.cm.gray)        

plt.imshow(l[200:220, 200:220], cmap=plt.cm.gray, interpolation='nearest')        





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
# Fancy indexing
lena[range(400), range(400)] = 255


