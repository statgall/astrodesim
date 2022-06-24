

def is_small(im1, im2):

size1 = im1.shape[0] * im1.shape[1]
siez2 = im2.shape[0] * im2.shape[1]

if size1 < size2:
     small_im = im1
     big_im = im2
else:
    small_im = im2
    big_im = im1

return small_im, big_im