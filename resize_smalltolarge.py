import numpy as np
from scipy.interpolate import interp2d

def resize_smalltolarge(im1, deltapix1, new_dim, deltapix2):
    
    """
    im1: image1 data
    deltapix1: pixel size from image1 (deg/pix)
    new_dim: number of pixels from image2 (pix)
    deltapix2: pixel size from image2 (deg/pix)
    
    IMAGE1: (1.3 mm) LESS PIXELS, BUT LARGE PIX SIZE (1500 PIXELS, 3.9E-7 DEG/PIX) -> WIDTH2 = 2.106"
    IMAGE2: (0.87 mm) MORE PIXELS, BUT SMALL PIX SIZE (2000 PIXELS, 2.8E-7 DEG/PIX) -> WIDTH1 = 2.016"
    
    RESIZING IMAGE1 TO MATCH IMAGE2 DIMS
    
    """

    # Works if number of pixels in image1 is less than the number of pixels in image2
    
    # Creates a temporary matrix of the same length and width as image 2
    # But, with the same pixel size as image1
    # New pixels in the temporary matrix are filled in with zeros
    # The rest of the matrix contains image1
    
    # Interpolates temporary matrix to get new image with image2 dims (number of pixels & pixel size)
    
    # returns resized image

    im1_dim = len(im1) # number of pixels from image1
    
    if im1_dim < new_dim: # checks that number of pixels in image1 < number of pixels in image2
        
        # Creates temporary matrix
        diff = int((new_dim - im1_dim)/2.) # computes pixel difference between images and divides it by 2
        
        pad_with = ((diff,diff), (diff, diff)) # number of empty pixels to surround the matrix
        const_val = ((0,0), (0,0)) # values to add to the empty pixels
        
        # np.pad() takes image1, adds extra pixels and fills them with zeros
        temp_matrix = np.pad(im1, pad_with, 'constant', constant_values=const_val)
        
    # Creates the coordinates of the temporary matrix with pixel size: deltapix1
    temp_width = len(temp_matrix) # in pixels
    temp_halfwidth = temp_width/2.*deltapix1 # in deg
    
    xcoords = np.linspace(-temp_halfwidth, temp_halfwidth, temp_width)
    ycoords = np.linspace(-temp_halfwidth, temp_halfwidth, temp_width) # update for images of different length

    # Associates the coordinates to the temporary matrix
    temp_im = interp2d(xcoords, ycoords, temp_matrix)

    # Creates the coordinates of the resized image
    new_halfdim = new_dim/2.*deltapix2 # in deg
    
    new_xcoords = new_ycoords = np.linspace(-new_halfdim, new_halfdim, new_dim)

    # Interpolates the temporary matrix into the final resized image
    new_im = np.array(temp_im(new_xcoords, new_ycoords))
    
    return new_im