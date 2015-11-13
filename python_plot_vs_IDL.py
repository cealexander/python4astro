import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import sys,os 
from mpl_toolkits.axes_grid1 import ImageGrid

font = {'family': 'verdana',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

st_time = datetime.now()
    

from scipy.io.idl import readsav

filepath1='/Users/cealexan/Dropbox/python_work/6nov2015_tresp_aia.sav'
s1=readsav(filepath1)

tresp=s1.tresp
logte=s1.logte
channels=s1.channels

tr94=tresp[0,]


filepath2='/Users/cealexan/Dropbox/python_work/e0_all_info_hydro.sav'
s2=readsav(filepath2)

lc=s2.lc0
new=[2,1,6,5,4,3]
lc=lc[new,]
ntemp0=s2.ntemp0
time=s2.ntime0
t211tr=tresp[4,]
m211=max(t211tr)
n211=t211tr/m211
tmin=time[0]
tmax=time[-1]
trange=tmax-tmin
tr1=5.0
tr2=8.0    
tr211=(n211*trange)+tmin 
c1=min(time, key=lambda x:abs(x-tmin))     
c2=min(time, key=lambda x:abs(x-tmax))     
cut1=np.where(time == c1)
cut2=np.where(time == c2)
    
#plt.fill(logte,tr94, facecolor='lime',edgecolor='lime')
#plt.xlim(5.,7.5)

#plt.figure(figsize=(15/2,23/2), dpi=80)                 
#plt.fill(10.**logte,tr94, facecolor='lime',edgecolor='lime')
#plt.xlim(10.**5.,10.**7.3)
#plt.xticks(np.arange(10.**5,10.**7.3,2e6))                            
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useOFFset=True)                                                       
                                                                                    
                                                                                                                                          
plt.figure(figsize=(15/2,23/2), dpi=80)  
plt.subplot(211) 
plt.fill(tr211,logte, facecolor='lime',edgecolor='lime')
plt.ylim([tr1,tr2])
plt.title(r'211$\AA$ response cf temp evolution',fontdict=font)
plt.ylabel('Log Temperature (K)',fontdict=font)
plt.plot(time[cut1[0]:cut2[0]+1],np.log10(ntemp0),'grey',linewidth=2.0)
plt.xticks([]) 
plt.subplot(212) 
plt.plot(time[cut1[0]:cut2[0]+1],(lc[4,cut1[0]:cut2[0]+1]/max(lc[4,cut1[0]:cut2[0]+1])),'lime',linewidth=2.0)
plt.text(2500,0.8,r'211$\AA$ Lightcurve', fontdict=font)
plt.xlabel('Time (s)',fontdict=font)
plt.ylabel('Normalized Intensity',fontdict=font)
plt.subplots_adjust(hspace=0.0)
plt.tick_params(axis='x', which='both', bottom='on', top='on',  labelbottom='on') 
plt.tick_params(axis='y', which='both', left='off', right='on') 
plt.yticks([])
plt.show() 
 
 
#plt.savefig("a211_plot_python.jpg",dpi=80)
 
 
 
 
 
 
 
 
 