import skimage as skim
import skimage.io as skImIo
import matplotlib.pyplot as plt
import numpy as np

my_image = skImIo.imread('panda.jpg')
my_image[0].shape

print(my_image.min(),my_image.max())
plt.imshow(my_image)
plt.imshow(my_image*0.01)

my_image[200:240,:, :] = [255,0,0]
plt.imshow(my_image)


generated_image = np.random.random([500,500])
plt.imshow(generated_image)   
print(generated_image) 

float_image = skim.img_as_float(my_image)
print(float_image.min(),float_image.max())

plt.imshow(float_image)


