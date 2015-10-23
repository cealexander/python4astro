from astropy.io import fits
from scipy.ndimage import gaussian_filter
import numpy as np
import matplotlib.pyplot as plt
# Create empty image
nx, ny = 512, 512
image1 = np.zeros((ny, nx))

# Set number of stars
n = 10000

# Generate random positions
r = np.random.random(n) * nx
theta = np.random.uniform(0., 2. * np.pi, n)

# Generate random fluxes
f = np.random.random(n) ** 2

# Compute position
x = nx / 2 + r * np.cos(theta)
y = ny / 2 + r * np.sin(theta)

# Add stars to image
# ==> First for loop and if statement <==
for i in range(n):
    if x[i] >= 0 and x[i] < nx and y[i] >= 0 and y[i] < ny:
        image1[y[i], x[i]] += f[i]

# Convolve with a gaussian
image2 = gaussian_filter(image1, 1)

# Add noise
image3=np.copy(image2)
image3 += np.random.normal(3., 0.01, image2.shape)

plt.figure()
plt.imshow(image1)
plt.show()
plt.figure()
plt.imshow(image2)
plt.show()
plt.figure()
plt.imshow(image3)
plt.show()

