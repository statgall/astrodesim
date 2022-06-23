import math
import numpy as np


"""

Take the flux intensities (per pixel) from two FITS image files and compute the dust emission spectral index (beta).

"""
def spectral_index_conversion(flux1, flux2, wavelength1, wavelength2):
#flux1 =     #flux intensity from the first FITS image file
#flux2 =     #flux intensity from the second FITS image file

#wavelength1 =     #wavelength (in mm) for the first image was captured as
#wavelength2 =      #wavelength (in mm) for the second image was captured as

flux_rat = math.log10(flux1 / flux2)

wavelength_rat = math.log(wavelength1 / wavelength2)

beta = flux_rat / wavelength_rat #beta is the new array of 'flux intensities' used to create a new image

