
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the PNG image
image = Image.open("canvas.png")
width = image.width
height = image.height

# Get pixel data
pixels = np.array(image)
#print(pixels)
print(f"{width}, {height}")

#RGB -> YCbCr
tmp_y_channel = list()
tmp_cb_channel = list()
tmp_cr_channel = list()

# Print pixel values
for row in pixels:
    #print(row)
    tmp_y = list()
    tmp_cb = list()
    tmp_cr = list()
    for pixel in row:
        #print(f"R:{pixel[0]} G:{pixel[1]} B:{pixel[2]} A:{pixel[3]}")
        y = 0.3 * pixel[0] + 0.6 * pixel[1] + 0.114 * pixel[2]
        cb =128 - (0.17 * pixel[0]) + (0.3 * pixel[1]) + (0.5 * pixel[2])
        cr = 128 + (0.5 * pixel[0]) + (0.419 * pixel[1]) + (0.08 * pixel[2])
        #print(f"Y:{round(y, 2)} Cb:{round(cb, 2)} Cr:{round(cr, 2)}")    
        tmp_y.append(round(y,2));
        tmp_cb.append(round(cb,2));
        tmp_cr.append(round(cr,2));
    tmp_y_channel.append(tmp_y);
    tmp_cr_channel.append(tmp_cb);
    tmp_cb_channel.append(tmp_cr);

f_y = "y.txt"
f_cb = "cb.txt"
f_cr = "cr.txt"

y_channel = np.array(tmp_y_channel)
cb_channel = np.array(tmp_cb_channel)
cr_channel = np.array(tmp_cr_channel)

np.savetxt(f_y, y_channel, fmt='%.2f')
np.savetxt(f_cb, cb_channel, fmt='%.2f')
np.savetxt(f_cr, cr_channel, fmt='%.2f')

original = image
y_image = Image.fromarray(y_channel)
cb_image = Image.fromarray(cb_channel)
cr_image = Image.fromarray(cr_channel)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(original, cmap='gray')
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(y_image, cmap='gray')
axes[1].set_title('Y-channel')
axes[1].axis('off')

axes[2].imshow(cb_image, cmap='gray')
axes[2].set_title('Cb')
axes[2].axis('off')

axes[3].imshow(cr_image, cmap='gray')
axes[3].set_title('Cr')
axes[3].axis('off')


plt.tight_layout()

plt.axis('off')  # Hide axes
plt.show()

#DCT:
