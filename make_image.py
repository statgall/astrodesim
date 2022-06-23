import numpy as np
import matplotlib as plt

def make_image(data):
    #Creates image for simulated observation

    fig = plt.figure(figsize = (8, 8))
    vmax = np.percentile(data, 99)
    vmin = np.percentile(data, 1)
    norm = ImageNormalize(vmin = vmin, vmax = vmax, stretch = AsinhStretch())
    snu = np.squeeze(data)

    im = plt.imshow(snu, origin = 'lower', cmap = 'inferno', norm = norm)

    return im