
# Imports
import numpy as np
import matplotlib.pyplot as plt
import pdb


# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(23/2,15/2), dpi=80)

# Create a new subplot from a grid of 1x1  (row, column, plot#)
plt.subplot(122)


a=[0,450]
b=[0,1000]
#make empty plot space
plt.plot(a,b, color='blue',linewidth=0)

cor=[150,270,390,660,720]
pho=[180,360,630,810,780]
#length=[50,100,200,300,400]
length = np.array([50,100,200,300,400], dtype="float32")

plt.scatter(50,150, s=200, color ='black',marker='*')
plt.scatter(50,180, s=100, color ='black', marker='^')

plt.scatter(100,270, s=200, color ='black',marker='*')
plt.scatter(100,360, s=100, color ='black', marker='^')

plt.scatter(200,390, s=200, color ='black',marker='*',facecolors='none', edgecolors='black')
plt.scatter(200,630, s=100, color ='black', marker='^',facecolors='none', edgecolors='black')
pdb.set_trace()


plt.scatter(300,660, s=200, color ='black',marker='*',facecolors='none', edgecolors='black')
plt.scatter(300,810, s=100, color ='black', marker='^',facecolors='none', edgecolors='black')

plt.scatter(400,720, s=200, color ='black',marker='*',facecolors='none', edgecolors='black')
plt.scatter(400,780, s=100, color ='black', marker='^',facecolors='none', edgecolors='black')



#x=np.arange(0,100,2)
#y=np.arange(100,600,10)
#plt.plot(x,y,color='red',ls='-',marker='*')
plt.xlim(a)
plt.ylim(b)
cfit=np.polyfit(length,cor,2)
all_length=np.arange(50,400,1)
fit_c=all_length*all_length*(cfit[0])+all_length*(cfit[1])+(cfit[2])
#fit_c=(length**2)*(cfit[0])+length*(cfit[1])+(cfit[2])
pfit=np.polyfit(length,pho,2)
fit_p=all_length*all_length*(pfit[0])+all_length*(pfit[1])+(pfit[2])

plt.plot(all_length,fit_p,color='red')
plt.plot(all_length,fit_c,color='red')
plt.title('335$\AA$ - 211$\AA$')
plt.xlabel('Loop length (Mm)')
plt.ylabel('Time Lag (s)')
#plt.savefig("idl_evivalent.eps",dpi=72)

plt.show()


































