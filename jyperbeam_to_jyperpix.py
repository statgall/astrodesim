def Jyperbeam_to_Jyperpix(header, data):
    
    convert = np.pi / 180 #deg to rads
    fwhm_to_sigma = 1. / (8 * np.log(2)) ** 0.5

    bmaj = header['BMAJ'] * convert
    bmin = header['BMIN'] * convert

    beam_area = 2. * np.pi * (bmaj * bmin) * fwhm_to_sigma * 2) # in staradians
    Jyperpix_data = data / beam_area
    
    return Jyperpix_data