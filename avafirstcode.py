import imageio
img = imageio.v3.imread('/home/avavivvilla/v.1/sections/cat_myelin/catsec_m105.jpg')
threshold = (img.max() * 0.5)
segmented_mask = (img > threshold).astype(float)
       
import matplotlib.pyplot as plt
plt.subplot(1,2,1) # create a figure with 1 x 2 subplots and create the 1st sub-figure 
plt.imshow(img) # display the img in the 1st subfigure
plt.subplot(1,2,2) # create a figure with 1 x 2 subplots and create the 2nd sub-figure 
plt.imshow(segmented_mask) # display the segmented_mask in teh 2snd sub-figure
plt.show()

#plt.savefig('/home/avavivvilla/')
