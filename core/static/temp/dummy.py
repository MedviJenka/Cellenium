import sys
from skimage.measure import compare_ssim
from skimage.transform import resize
from scipy.ndimage import imread

# get two images - resize both to 1024 x 1024
img_a = resize(imread(sys.argv[1]), (2**10, 2**10))
img_b = resize(imread(sys.argv[2]), (2**10, 2**10))

# score: {-1:1} measure of the structural similarity between the images
score, diff = compare_ssim(img_a, img_b, full=True)
print(score)