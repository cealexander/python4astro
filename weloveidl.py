#------------------------------------------------
###### our functions for IDL replacements
#------------------------------------------------


# from astropy.convolution import convolve, Box1DKernel

def smooth(data, width):
    return convolve(data,Box1DKernel(width))
