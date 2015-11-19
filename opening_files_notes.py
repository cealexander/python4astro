
#### finding files

import sys,os
import glob
fdir ='/Users/cealexan/sunpy/data/sample_data/'
filenames=sorted(glob.glob(fdir + '*.fits'))
for file in filenames:
    print os.path.basename(file)

filename=filenames[1]

########  FITS files
import astropy.io.fits as fits
fname='/Users/cealexan/Documents/work/projects/NRLvsOBS/aia.lev1.171A_2010-12-11T02_24_00.34Z.image_lev1.fits'
data=fits.open(fname)
header=data[0].header
image = data[0].data
image.shape






####### IDL .sav files

from scipy.io.idl import readsav

filepath1='/Users/cealexan/Dropbox/python_work/6nov2015_tresp_aia.sav'
s1=readsav(filepath1,verbose=True)

tresp=s1.tresp
logte=s1.logte
channels=s1.channels

#######
###############################################
#file I/O

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()


#######
a = "  I ain't afraid of no ghost.    "
a = a.rstrip() # strip whitespace on the right (trailing)
a = a.lstrip() # strip whitespace on the left (leading)
a = a.strip()  # strip whitespace from front and back



text = "X-DSPAM-Confidence:    0.8475"
print text
num=text.find('0')
print text[num :]

xfile = open('mbox.txt')
for line in xfile:
    print line

#######



#######



#######