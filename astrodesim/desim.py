from astrodesim import upload_fits
from astrodesim import is_small
from astrodesim import resize_smalltolarge
from astrodesim import spectral_index_map
from astrodesim import make_image

def desim(file1, file2):
    """
    Function outputs a dust emission spectral index map

    Args: 
        file1 (str): path to fits file with image at one wavelength
        file2 (str): path to fits file with same image at another wavelength
    """
    header1, sim_data1 = upload_fits(file1) 
    header2, sim_data2 = upload_fits(file2)

    smallim, deltapix1, new_header, bigim, new_dim, deltapix2, bigheader = is_small(sim_data1, sim_data2, header1, header2)

    new_im = resize_smalltolarge(smallim, deltapix1, new_dim, deltapix2)

    desim = spectral_index_map(new_im, bigim, new_header, bigheader)

    make_image(desim)

# need to update header file to match data changes