from astropy.io import fits


def download_fits(path, wavelength):
    
    file = path + '/isoscat_' + wavelength + 'mm_inc45.fits'
    with fits.open(file) as hdul:
        sim_data = hdul[0].data[0,0,:,:]
        header = hdul[0].header
    
    return sim_data, header