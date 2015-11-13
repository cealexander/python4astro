notes:
    
# import pdb



pdb.set_trace()



c



###############

# ideas for future meetings

# -- movies! 

# -- reading in data cubes

# -- lists vs arrays

# -- reading text files, skipping header lines.

# -- colors! maps and line colors :)

# -- image processing - box-car!!!


from numarray.convolve import boxcar

sflux = boxcar(data, (100,)) # smooth flux array



def smooth1D(image,width=2,axis=0,decimate=False):
    data=convolve1d(image,np.ones((width,))/width,mode='wrap',axis=axis)
    
    if decimate:
        data=boxdec1D(data,width=width,axis=axis)
        return data
        






# order of arrays
# notation





# need to download 
ffmpeg






#array.reshape() ie. rebin

#axis =  instead of dim =


# python .sav equivalent pickle?  --> save as fits?






###### add to cheat sheet

# precision on %f stuff

# how to quickly close all windows   plt.close('all')

# how to pause programs